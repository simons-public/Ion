""" Setup up the launch environment """
from os import path
from .logger import log

def game_setup(game):
    """ Sets up the game prefix for launching """

    if not path.isdir(game.prefix):
        build_prefix(game)

def build_prefix(game):
    """ Builds the game prefix """
    pass
