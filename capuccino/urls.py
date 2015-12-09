from handlers.handlers import ExampleHandler
from handlers.handlers import BaseHandler

urls = [
	(r'/example', ExampleHandler),
	(r'/', BaseHandler),

]
