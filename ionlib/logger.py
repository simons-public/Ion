""" Handles logging for Ion """

import os
import logging
from . import conf

color_map = {
    'reset': '\x1b[0m', #plain
    logging.DEBUG: '\033[92m', #green
    logging.INFO: '\033[94m', #blue
    logging.WARNING: '\033[91m', #red
    logging.CRITICAL: '\033[101m', #red bg
    }

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=os.path.join(conf.ion.data_dir, 'ion.log'),
                    filemode='w'
                   )

console = logging.StreamHandler()
formatter = logging.Formatter(f'{color_map[10]} %(asctime)s %(name)s %(levelname)s %(message)s {color_map["reset"]}')
console.setFormatter(formatter)
console.setLevel(logging.INFO)

logging.getLogger('').addHandler(console)

log = logging.getLogger()
