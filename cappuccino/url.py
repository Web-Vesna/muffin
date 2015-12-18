#from handlers import session
import session

# Add routes

routes = [
	('GET', '/', session.test_handler),

]

