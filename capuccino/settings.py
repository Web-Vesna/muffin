# This is project settings file

import os
import tornado
from tornado.options import define, options

from config import CAPPUCCINO, CHEESECAKE
from config_parser import ServiceConfig

# DEFINE SERVICES
# Capuccino is the current service. You can define 
# its name to use as global by setting 'name' attribute
# (default name is cappuccino). To use cheesecake in project
# use define function below.
cappuccino = ServiceConfig(CAPPUCCINO)
cappuccino.secret_key = os.urandom(64)

# Cheesecake service is the authorization service
# Default name is session. You can also change it by setting
# 'name' attribute.
cheesecake = ServiceConfig(CHEESECAKE)
if not hasattr(cheesecake, 'name'): setattr(cheesecake, 'name', 'session')

define('port', default=cappuccino.port, help='run on the given port', type=int)
define('debug', default=False, help='debug mode')
define(cheesecake.name, default=cheesecake, help='authorization service Cheesecake')
tornado.options.parse_command_line()


# PROJECT SETTINGS
settings = {}
settings['cookie_secret'] = os.environ.get('CAPPUCCINO_SECRET_KEY') or cappuccino.secret_key
settings['xsrf_cookies'] = True


#if options.config:
#	tornado.options.parse_config_file(options.config)
