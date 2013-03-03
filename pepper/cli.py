'''
A CLI interface to an instance of salt-api's REST interface

'''
import ConfigParser
import logging
import optparse
import os

try:
    from logging import NullHandler
except ImportError: # Python < 2.7
    class NullHandler(logging.Handler):
        def emit(self, record): pass

from . import rest
from . import version

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(NullHandler())
logger.addHandler(logging.StreamHandler())

SALT_API_URL = os.environ.get('SALTAPIURL')

HOME = os.path.expanduser("~")
RCFILE = '.pepperrc'

def get_parser():
    '''
    Return a basic optparse parser object
    '''
    parser = optparse.OptionParser(
            description=__doc__,
            usage="%prog [opts]",
            version=version.__version__)

    parser.add_option("-v", dest="verbose", default=0, action="count",
            help="increment output verbosity; may be specified multiple times")

    return parser

class PepperOptsMixin(object):
    def __init__(self):
        parser = self.parser

        optgroup = optparse.OptionGroup(parser, "Pepper Options",
                "Pepper is a direct interface to salt-api's REST interface")

        optgroup.add_option('--debug', dest='debug', action='store_true',
                help='Only output what will be done.')

        parser.add_option_group(optgroup)

def validate_opts(parser):
    opts, args = parser.parse_args()

    # Collect all servers
    if not opts.debug:
        parser.error("You must specify at least one destination.")

    return opts, args

def get_config():
    '''
    Read a user's configuration file
    '''
    f=os.path.join(HOME, RCFILE)
    config = ConfigParser.ConfigParser()
    config.read(f)
    sections = config.sections()

def main():
    '''
    Collect all the given CLI parameters and make a request to salt-api
    '''
    parser = get_parser()
    opts, args = validate_opts(parser)

    logger.level = max(logging.ERROR - (opts.verbose * 10), 1)
    logger.warning("HEYOOO")
