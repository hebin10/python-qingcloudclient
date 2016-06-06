# -*- coding: utf-8 -*-

import logging

from qingcloudclient.cli.base import BaseCommand
from qingcloudclient import connection
from qingcloudclient import utils


class TerminateInstances(BaseCommand):
    log = logging.getLogger(__name__)

    action = 'TerminateInstances'
    time_stamp = utils.get_utc_time_stamp()
    array_params_set = ['instances']
    other_params_set = ['zone']

    def get_description(self):
        return 'terminate instance(s)'

    def get_parser(self, prog_name):
        parser = super(TerminateInstances, self).get_parser(prog_name)

        parser.add_argument(
            "--instances",
            metavar="<instance1_id,instance2_id,...>",
            help="Id of instances to terminate",
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
