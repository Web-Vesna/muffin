
from app import init_server
from app.settings import loop

if __name__ == "__main__":
	loop.run_until_complete(init_server(loop))
	loop.run_forever()
