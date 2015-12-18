import asyncio

from aiohttp import web
from app.url import routes
from settings import app_config

@asyncio.coroutine
def init_server(loop):
	app = web.Application(loop=loop)
	for route in routes:
		app.router.add_route(route[0], route[1], route[2])
	server = yield \
		from loop.create_server(app.make_handler(), app_config.ip, app_config.port)
	#print('Server started at ' + str(app_config.ip) + ':' + str(app_config.port))
	return server
