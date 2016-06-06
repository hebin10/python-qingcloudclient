# -*- coding: utf-8 -*-

import logging
import sys

from qingcloudclient.cli.base import BaseCommand
from qingcloudclient import connection
from qingcloudclient import utils

DEFAULT_INSTANCES_COUNT = 1
DEFAULT_NEED_NEWSID = 0
DEFAULT_NEED_USERDATA = 0
DEFAULT_USERDATA_PATH = '/etc/qingcloud/userdata'
DEFAULT_USERDATA_FILE = '/etc/rc.local'


class RunInstances(BaseCommand):
    log = logging.getLogger(__name__)

    action = 'RunInstances'
    time_stamp = utils.get_utc_time_stamp()
    array_params_set = ['vxnets', 'volumes']
    other_param_set = ['count', 'cpu', 'image_id', 'instance_class',
                       'instance_name', 'instance_type', 'login_keypair',
                       'login_mode', 'login_passwd', 'memory', 'need_newsid',
                       'need_userdata', 'security_group', 'time_stamp',
                       'userdata_file', 'userdata_path', 'userdata_type',
                       'userdata_value', 'zone']

    def get_description(self):
        return 'command to run instance(s)'

    def get_parser(self, prog_name):
        parser = super(RunInstances, self).get_parser(prog_name)

        # For specific arguments
        parser.add_argument(
            "--zone",
            required=True,
            metavar="<zone>",
            help="Zone of instances",
        )
        parser.add_argument(
            "--image_id",
            metavar="<image-id>",
            required=True,
            help="Id of the image used to run instances",
        )
        parser.add_argument(
            "--instance_type",
            metavar="<instance-type>",
            choices=["c1m1", "c1m2", "c1m4", "c2m2", "c2m4", "c2m8", "c4m4",
                     "c4m8", "c4m16"] + \
                    ["small_b", "small_c", "medium_a", "medium_b",
                     "medium_c", "large_a", "large_b", "large_c"],
            help="Type of the instances,like c1m1, c1m2...",
        )
        parser.add_argument(
            "--cpu",
            type=int,
            metavar="<instance-cpu>",
            choices=[1, 2, 4, 8, 16],
            help="Number of cups of each instance. Valid value: "
                 "1, 2, 4, 8, 16",
        )
        parser.add_argument(
            "--memory",
            type=int,
            metavar="<instance-memory>",
            choices=[1024, 2048, 4096, 6144, 8192, 12288, 16384, 24576, 32768],
            help="Memory of each instance. Valid value: "
                 "1024, 2048, 4096, 6144, 8192, 12288, 16384, 24576, 32768",
        )
        parser.add_argument(
            "--count",
            type=int,
            metavar="<instances-count>",
            help="Number of instances to create, Default 1"
        )
        parser.add_argument(
            "--instance_name",
            metavar="<instance-name>",
            help="The name of the instance(s)",
        )
        parser.add_argument(
            "--login_mode",
            required=True,
            choices=["keypair", "passwd"],
            metavar="<login-mode>",
            help="Login mode",
        )
        parser.add_argument(
            "--login_keypair",
            metavar="<login-keypair>",
            help="The private key id for login",
        )
        parser.add_argument(
            "--login_passwd",
            metavar="<login-passwd>",
            help="The password for login",
        )
        parser.add_argument(
            "--vxnets",
            metavar="<vxnet1_id,vxnet2_id,...>",
            help="The id of the private network, which the instances "
                 "will join in. If not specify, the instances will not be "
                 "added to any network. Please use a ',' to separate value, "
                 "like --vxnets vxnet-123,vxnet-456",
        )
        parser.add_argument(
            "--security_group",
            metavar="<security-group>",
            help="The firewall of the instances",
        )
        parser.add_argument(
            "--volumes",
            metavar="<volume1_id,volume2_id,...>",
            help="The volume id",
        )
        parser.add_argument(
            "--need_newsid",
            type=int,
            choices=[0, 1],
            default=DEFAULT_NEED_NEWSID,
            metavar="<need-newsid>",
            help="Create new sid, only for windows. Default is %s, "
                 " doesn't create new sid" % DEFAULT_NEED_NEWSID,
        )
        parser.add_argument(
            "--need_userdata",
            type=int,
            choices=[0, 1],
            default=DEFAULT_NEED_USERDATA,
            metavar="<need-userdata>",
            help="Userdata feature. Default is %s, not use." \
                 % DEFAULT_NEED_USERDATA,
        )
        parser.add_argument(
            "--userdata_type",
            metavar="<userdata-type>",
            choices=["plain", "exec", "tar"],
            help="Userdata type. Valid value: plain, exec or tar",
        )
        parser.add_argument(
            "--userdata_value",
            metavar="<userdata-value>",
            help="The value of userdata",
        )
        parser.add_argument(
            "--instance_class",
            metavar="<instance-class>",
            choices=["0", "1"],
            help="The performance of instance. Valid value: 0 or 1, "
                 "and 1 represents higher performance",
        )
        parser.add_argument(
            "--userdata_path",
            metavar="<userdata-path>",
            help="Userdata and MetaData file path, Default is %s" \
                 % DEFAULT_USERDATA_PATH,
        )
        parser.add_argument(
            "--userdata_file",
            metavar="<userdata-file>",
            help="Excutable file path, when userdata_type is 'exec', Default"
                 "is %s" % DEFAULT_USERDATA_FILE,
        )
        return parser

    def take_action(self, parsed_args):
        params = {}

        for attr in self.array_params_set:
            utils.parse_array_value(attr, parsed_args, params)

        for attr in self.other_param_set + self.common_params_set:
            if attr in parsed_args:
                val = getattr(parsed_args, attr, None)
                if val:
                    params[attr] = val

        params['action'] = self.action
        params['time_stamp'] = self.time_stamp

        # check params
        # For instance_type and cpu, memory
        if 'instance_type' not in params:
            if ('cpu' not in params) or ('memory' not in params):
                self.log.info('"run-instances" command need whether'
                              ' "instance_type" or "cpu" and "memory" '
                              'arguments. If both specified, "cpu" and '
                              ' "memory" arguments will take effect.')
                sys.exit(-1)

        # For login_mode
        if params['login_mode'] == 'keypair' and 'login_keypair' not in params:
            self.log.info('When login_mode is keypair, the argument '
                          '"login_keypair" is required!')
            sys.exit(-1)
        if params['login_mode'] == 'passwd' and 'login_passwd' not in params:
            self.log.info('When login_mode is passwd, the argument '
                          '"login_passwd" is required!')
            sys.exit(-1)

        # For volumes
        if 'count' in params and params['count'] != 1 and 'volumes' in params:
            self.log.info("When specified 'volumes' argument, 'count' must "
                          "be 1 or do not specify 'count'")
            sys.exit(-1)

        path = utils.get_signed_params(
            params,
            params['secret_access_key'],
            params['signature_method']
        )

        response = connection.get_response(path)
        if response.status == 200:
            self.log.info(utils.string_to_json(response.read()))
        else:
            self.log.info('api request status: %s, reason: %s' % \
                          (response.status, response.reason))
