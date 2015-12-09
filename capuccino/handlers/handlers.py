import tornado.web
import cbor

from tornado.httpclient import HTTPRequest, AsyncHTTPClient
from tornado import gen
from settings import session


# Example handler
class BaseHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def get(self):
		client = AsyncHTTPClient()
		request = HTTPRequest(url=address.addr(), method='POST', \
				body=cbor.dumps([1,"test", 1]))
		response = yield client.fetch(request)
		self.write(response.body)
		self.finish()
		




