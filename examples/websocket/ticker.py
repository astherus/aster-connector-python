import time
import logging
from aster.lib.utils import config_logging
from aster.websocket.client.stream import WebsocketClient as Client

config_logging(logging, logging.DEBUG)

def message_handler(message):
    print(message)

my_client = Client()
my_client.start()

my_client.ticker(
    id=13,
    callback=message_handler,
    symbol="btcusdt",
)

time.sleep(2)

logging.debug("closing ws connection")
my_client.stop()