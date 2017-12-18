"""Troubleshooting OpenSSH client-server issues.

Script will check:
[server]
authorized_keys presence
config: allow password
config: allow public_key
config: chipers

[client]

[client.private_key]
presence
permissions

[client.public_key]
presence
permissions
"""
import sys
import logging


logging.basicConfig(level=logging.DEBUG)

CLIENT = 'client'
SERVER = 'server'

MODES = {
    'client': CLIENT,
    'server': SERVER
}


class OpenSSHChecker():
    """OpenSSH troubleshooting."""

    name = 'OpenSSHChecker'

    def __init__(self, mode=MODES[CLIENT]):
        """Create logger instance."""
        self.logger = logging.getLogger('.')
        self.debug('{} initialized in {} mode..'.format(self.name, mode))

    def debug(self, message):
        """Log debug message."""
        self.logger.debug(message)

    def run(self):
        """Launch troubleshooting process."""
        return True
    
    @staticmethod
    def print_usage():
        """Print usage for class."""
        message = (
            'Usage: check.py mode;\n'
            '  Arguments: mode; Could be one of: server, client'
        )
        print(message)

if __name__ == "__main__":
    MODE = ''
    if len(sys.argv)>1:
        MODE = sys.argv[1]

    if MODE not in MODES:
        OpenSSHChecker.print_usage()
        sys.exit(1)

    helper = OpenSSHChecker(mode=MODE)
    helper.run()
