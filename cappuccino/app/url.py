#from handlers import session
import app.session

# Add routes

routes = [
	('GET', '/', app.session.test_handler),

]

