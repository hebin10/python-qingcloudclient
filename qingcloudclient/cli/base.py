# -*- coding: utf-8 -*-

import logging

from cliff.command import Command


class BaseCommand(Command):
    log = logging.getLogger(__name__)
    common_params_set = ['secret_access_key', 'signature_method', 'version',
                         'signature_version', 'access_key_id']

    def get_parser(self, prog_name):
        """Deal with some common arguments """

        parser = super(BaseCommand, self).get_parser(prog_name)
        # API version
        parser.add_argument(
            "--api_version",
            dest="version",
            metavar="<api-version>",
            choices=["1"],
            default="1",
            help="API to use, Valid 1, Default 1",
        )
        parser.add_argument(
            "--secret_access_key",
            required=True,
            metavar="<secret-access-key>",
            help="Secret access key",
        )
        parser.add_argument(
            "--access_key_id",
            required=True,
            metavar="<access-key-id>",
            help="Access Key ID",
        )
        parser.add_argument(
            "--signature_method",
            metavar="<signature-method>",
            choices=["HmacSHA256", "HmacSHA1"],
            default="HmacSHA256",
            help="Signature method, Valid: HmacSHA256, HmacSHA1"
        )
        parser.add_argument(
            "--signature_version",
            metavar="<signature-version>",
            choices=["1"],
            default="1",
            help="Signature version, Valid 1, Default 1",
        )
        return parser

    def take_action(self, parsed_args):
        return
