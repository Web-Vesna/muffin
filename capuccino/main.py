import tornado.ioloop
import tornado.web

from tornado import httpserver
from tornado.options import options

from urls import urls
from settings import settings


class TornadoApplication(tornado.web.Application):
	def __init__(self):
		tornado.web.Application.__init__(self, urls, **settings)

def main():
	application = TornadoApplication()
	server = httpserver.HTTPServer(application)
	server.listen(options.port)
	tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
	main()
