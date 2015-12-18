import asyncio

from aiohttp import web
from settings import loop
from settings import app_config
from protocol import Protocol
from url import routes


@asyncio.coroutine
def init():
	app = web.Application(loop=loop)
	for route in routes:
		app.router.add_route(route[0], route[1], route[2])
	server = yield \
		from loop.create_server(app.make_handler(), app_config.ip, app_config.port)

	return server
	

def main():
	print('Server started at ' + str(app_config.ip) + ':' + str(app_config.port))
	loop.run_until_complete(init())
	loop.run_forever()



if __name__ == "__main__":
	main()
