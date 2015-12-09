import tornado.web
import cbor

from tornado.options import options
from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest
from tornado import gen
from settings import cheesecake as session

class Address:
	def __init__(self):
		self.ip = session.ip
		self.port = session.port

	def addr(self):
		return 'http://' + str(self.ip) + ':' + str(self.port) + '/'

address = Address()
print address.addr()

class ExampleHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def get(self):
		client = AsyncHTTPClient()
		response = yield client.fetch('http://www.google.com')
		self.write(response.body)
		self.finish()


class BaseHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def get(self):
		client = AsyncHTTPClient()
		request = HTTPRequest(url=address.addr(), method='POST', \
				body=cbor.dumps([1,"test", 1]))
		response = yield client.fetch(request)
		self.write(response.body)
		self.finish()
		


