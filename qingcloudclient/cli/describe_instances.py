# -*- coding: utf-8 -*-

import logging

from qingcloudclient.cli.base import BaseCommand
from qingcloudclient import connection
from qingcloudclient import utils


class DescribeInstances(BaseCommand):
    log = logging.getLogger(__name__)

    action = 'DescribeInstances'
    time_stamp = utils.get_utc_time_stamp()

    array_params_set = ['instances', 'image_id', 'instance_type',
                        'status', 'tags']

    other_params_set = ['instance_class', 'search_word',
                        'verbose', 'offset', 'limit', 'zone']

    def get_description(self):
        return 'get instance(s) information'

    def get_parser(self, prog_name):
        parser = super(DescribeInstances, self).get_parser(prog_name)

        # For specific arguments
        parser.add_argument(
            "--instances",
            metavar="<instance1ID,instance2ID,...>",
            help="Instances IDs",
        )
        parser.add_argument(
            "--image_ids",
            metavar="<image_id1,image_id2,...>",
            help="Image IDs",
        )
        parser.add_argument(
            "--instance_types",
            metavar="<instance_type1,instance_type2,...>",
            help="Instance type",
        )
        parser.add_argument(
            "--instance_class",
            type=int,
            choices=[0, 1],
            metavar="<instance-class>",
            help="Instance class",
        )
        parser.add_argument(
            "--status",
            metavar="<status1,status2,...>",
            choices=["pending", "running", "stopped", "suspended",
                     "terminated", "ceased"],
            help="Status of instances, Valid: pending, running, stopped, "
                 "suspended, terminated, ceased",
        )
        parser.add_argument(
            "--search_word",
            metavar="<search-word>",
            help="Keyword for search, support id and name of instance",
        )
        parser.add_argument(
            "--tags",
            metavar="<tag1,tag2,...>",
            help="Tags that instances bound to",
        )
        parser.add_argument(
            "--V",
            dest='verbose',
            type=int,
            metavar="<verbose>",
            help="Detail message, 1 for more detail message",
        )
        parser.add_argument(
            "--offset",
            type=int,
            metavar="<offset>",
            help="Offset, default is 0",
        )
        parser.add_argument(
            "--limit",
            type=int,
            metavar="<limit>",
            help="Length of retruned data, default is 20, max 100",
        )
        parser.add_argument(
            "--zone",
            required=True,
            metavar="<zone>",
            help="Zone of instances",
        )
        return parser

    def take_action(self, parsed_args):
        params = {}
        for arg in self.array_params_set:
            utils.parse_array_value(arg, parsed_args, params)

        for arg in self.other_params_set + self.common_params_set:
            if arg in parsed_args:
                val = getattr(parsed_args, arg, None)
                if val:
                    params[arg] = val

        params['action'] = self.action
        params['time_stamp'] = self.time_stamp

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
