""" Handles wine commands """

import os
import subprocess
from . import conf
from .logger import log

#pylint: disable = W0102

def run(cmd, output=None, env=dict(os.environ)):
    """ Runs a command in with wine """

    if output:
        subprocess.check_output([conf.wine.wineloader] + cmd, env=env)
        return

    wine_logfile = os.path.join(conf.ion.logs_dir, 'wine.log')
    with open(wine_logfile, 'w') as logfile:
        try:
            subprocess.call([conf.wine.wineloader] + cmd, env=env, stderr=logfile)
        finally:
            logfile.flush()


def server(cmd, env=dict(os.environ)):
    """ only wait for cmd """
    arg_map = {
        'wait': '-w',
        'kill': '-k',
        }

    log.info(f'Starting wineserver with {arg_map[cmd]}')
    subprocess.Popen([conf.wine.wineserver, arg_map[cmd]], env=env)


def tricks(verb, env=dict(os.environ)):
    """ Run winetricks """
    pass
