# This is project settings file

import os
import tornado
from tornado.options import define, options

from config import CAPPUCCINO, SESSION
from config_parser import ServiceConfig

###### APPLICATION OPTIONS
# Cappuccino service (application)
cappuccino = ServiceConfig(CAPPUCCINO)
# Only in debug mode
if not hasattr(cappuccino, 'secret_key'):
	cappuccino.secret_key = os.urandom(64)

# Authorization and session service
session = ServiceConfig(SESSION)
if not hasattr(session, 'name'): setattr(session, 'name', 'session')


# Next lines defines options to use in application
define('port', default=cappuccino.port, help='run on the given port', type=int)
define('debug', default=False, help='debug mode')
define(session.name, default=session, help='authorization and session service')
tornado.options.parse_command_line()


##### SET PROJECT SETTINGS
settings = {}
settings['cookie_secret'] = os.environ.get('CAPPUCCINO_SECRET_KEY') or cappuccino.secret_key
settings['xsrf_cookies'] = True


#if options.config:
#	tornado.options.parse_config_file(options.config)
