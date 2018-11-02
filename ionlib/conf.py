""" Provides configuration data for Ion """

import sys
import shutil
from os import path, environ, makedirs, getcwd
from collections import namedtuple
from configparser import ConfigParser

#pylint: disable=C0103

ION_VERSION = '1.0.0'
ION_DESC = 'Description'

ion = namedtuple('IonConfig', 'data_dir, logs_dir, cache_dir, config_dir')(
    path.join(environ.get('XDG_DATA_HOME') or path.expanduser('~/.local/share'), 'ion'),
    path.join(environ.get('XDG_DATA_HOME') or path.expanduser('~/.local/share'), 'ion', 'logs'),
    path.join(environ.get('XDG_CACHE_HOME') or path.expanduser('~/.cache'), 'ion'),
    path.join(environ.get('XDG_CONFIG_HOME') or path.expanduser('~/.config'), 'ion'),
    )

# make ion dirs
[makedirs(d, exist_ok=True) for i, d in zip(ion._fields, ion) if 'dir' in i]

# read configs in cwd, ion dir, ion config_dir
games = ConfigParser()
games['DEFAULT'] = {
    'append_args': '',
    'corefonts': 'true',
    'dvxk': 'true',
    'esync': 'true',
    'environment': '',
    'winetricks': '',
    'win32_prefix': 'false',
    'overrides': 'd3d11=n;d3d10=n;d3d10core=n;d3d10_1=n;dxgi=n'
    }
games.read([
    path.join(getcwd(), 'games.ini'),
    path.join(path.dirname(sys.argv[0]), 'games.ini'),
    path.join(ion.config_dir, 'games.ini'),
    ])

# steam config
steam = namedtuple('SteamConfig', 'overlay, tenfoot')(
    environ.get('SteamNoOverlayUI'),
    environ.get('SteamTenfoot'),
    )

# wine config
wine = namedtuple('WineConfig', 'wineserver, wineloader, wine, winetricks')(
    shutil.which('wineserver'),
    shutil.which('wine'),
    shutil.which('wine'),
    shutil.which('winetricks'),
    )
