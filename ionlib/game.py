""" Game object for launching with Ion """

import os
import sys
from . import conf
from . import cmdline

class Game():
    def __init__(self):
        try:
            self.id = os.environ['SteamGameId']
        except KeyError:
            self.id = '0'
        self.compat_path = os.environ['STEAM_COMPAT_DATA_PATH']
        self._set_config()
        self._set_cmd()
        self._set_prefix()
        self._set_environ()

    def _set_config(self):
        """ Sets the game configuration """
        if self.id in conf.games:
            self.config = conf.games[self.id]
        else:
            self.config = conf.games['DEFAULT']

    def _set_cmd(self):
        """ Sets the games command line """

        # don't change arguments for iscriptevaluator
        if 'legacycompat' in cmdline.args.path:
            self.cmd = [cmdline.args.path]
            return

        cmd = cmdline.args.path
        replace = self.config.get('replace_cmd')
        append = self.config.get('append_args')

        if replace:
            old, new = replace.split(',')
            cmd = cmd.replace(old.strip(), new.strip())
        self.cmd = [cmd]

        if append:
            add_args = append.split(',')
            self.cmd += add_args

    def _set_prefix(self):
        """ Sets the game prefix """
        if self.config.getboolean('win32_prefix'):
            self.prefix = os.path.join(self.compat_path, 'pfx32')
        else:
            self.prefix = os.path.join(self.compat_path, 'pfx')

    def _set_environ(self):
        """ Sets the game environment """
        env = dict(os.environ)
        env['WINEPREFIX'] = self.prefix
        env['WINEDEBUG'] = '+timestamp,+pid,+tid,+seh,+debugstr,+module'

        overrides = self.config.get('overrides')
        environment = self.config.get('environment')
        esync = self.config.getboolean('esync')
        if overrides:
            env['WINEDLLOVERRIDES'] = overrides

        if esync:
            env['WINEESYNC'] = '1'

        if environment:
            # parse environment values:
            environment = dict(x.split('=') for x in environment.strip().split('\n'))
            env = {**env, **environment}
        self.env = env

    def __repr__(self):
        rep = '<Game:\n'
        rep += f'id: {self.id}\n'
        rep += f'env: {self.env}\n'
        rep += f'compat_path: {self.compat_path}\n'
        rep += f'prefix: {self.prefix}\n'
        rep += f'config: {self.config}\n'
        rep += f'command: {self.cmd}\n'
        rep += f'args: {sys.argv}\n'
        rep += '>\n'
        return rep
