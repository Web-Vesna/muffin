import tornado.web

from tornado.httpclient import AsyncHTTPClient
from tornado import gen

class ExampleHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def get(self):
		client = AsyncHTTPClient()
		response = yield client.fetch('http://www.google.com')
		self.write(response.body)
		self.finish()

'''
class SessionHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def get(self):
		client = httpclient.AsyncHTTPClient()
		response = yield gen.Task(client.fetch, 'http://google.com')
		self.write(response.body)
		self.finish()

'''
