from handlers.handlers import TCPHandler
from handlers.handlers import BaseHandler

urls = [
	(r'/', BaseHandler),
	(r'/test', TCPHandler),

]
