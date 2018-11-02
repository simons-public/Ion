""" Handle command line arguments for Ion """

from argparse import ArgumentParser
from . import conf

def get_args():
    """ Returns argparser arguments """

    modes = [
        'run',
        'waitforexitandrun',
        'getcompatpath',
        'getnativepath',
    ]

    parser = ArgumentParser(description=conf.ION_DESC)

    parser.add_argument('mode', type=str, help=' | '.join(modes))
    parser.add_argument('path', type=str, help='path to run', nargs='?')
    parser.add_argument('test', type=str, nargs='?')
    parser.add_argument('--get-current-step')

    return parser.parse_args()

#pylint: disable=C0103
args = get_args()
