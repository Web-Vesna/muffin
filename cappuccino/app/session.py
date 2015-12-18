import asyncio
import settings

from aiohttp import web
from .protocol import Protocol

protocol = Protocol()

#print(settings.session)


@asyncio.coroutine
def test_handler(request):
	reader, writer = \
		yield from asyncio.open_connection(settings.session.ip, \
					settings.session.port, loop=settings.loop)
	writer.write(protocol.encode([39, "test", 1]))
	text = yield from reader.read(6)
	text = protocol.decode(text)
	#text = 'Hello, World'
	return web.Response(body=str(text).encode('utf-8'))
