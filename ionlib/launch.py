""" Launch a game from Steam """

from . import wine
from . import setup
from .logger import log
from .cmdline import args
from .game import Game

def get_path():
    """ Returns the wine path (native or compat) """

    command = ['winepath', args.path]
    if 'compat' in args.mode:
        command.insert(1, '-w')

    wine.run(command)

def run(wait=False):
    """ Run game fix """
    game = Game()
    setup.game_setup(game)

    log.info(game)
    if wait:
        wine.server('wait', env=game.env)
    wine.run(game.cmd, env=game.env)
