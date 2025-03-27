
import time
import logging
from aster.lib.utils import config_logging
from aster.websocket.client.stream import WebsocketClient as Client

config_logging(logging, logging.DEBUG)

def message_handler(message):
    print(message)

my_client = Client()
my_client.start()

my_client.diff_book_depth(
    symbol="btcusdt",
    speed=100,
    id=1,
    callback=message_handler,
)

time.sleep(2)

logging.debug("closing ws connection")
my_client.stop()
