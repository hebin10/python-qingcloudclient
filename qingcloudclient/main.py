# -*- coding: utf-8 -*-

import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


class QingcloudClient(App):
    def __init__(self):
        super(QingcloudClient, self).__init__(
            description='Test CLI for QingCloud API',
            version='1.0',
            command_manager=CommandManager('qingcloudclient.instance'),
            deferred_help=True,
        )

    def initialize_app(self, argv):
        self.LOG.debug('Initial qingcloudclient')

    def prepare_to_run_command(self, cmd):
        self.LOG.debug('Prepare to run command: %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.LOG.debug('Clean up  command: %s', cmd.__class__.__name__)
        if err:
            self.LOG.debug('got an error: %s', err)


def main():
    cmd = QingcloudClient()
    return cmd.run(sys.argv[1:])


if __name__ == '__main__':
    sys.exit(main())
