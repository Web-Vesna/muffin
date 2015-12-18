import asyncio

from config_parser import ServiceConfig
from config import SESSION
from config import CAPPUCCINO

# Session and authorizatio service
session = ServiceConfig(SESSION)


# Application configs
app_config = ServiceConfig(CAPPUCCINO)


# Application loop
loop = asyncio.get_event_loop()
