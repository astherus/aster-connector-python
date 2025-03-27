import time
import logging
from aster.lib.utils import config_logging
from aster.websocket.client.stream import WebsocketClient as Client

config_logging(logging, logging.DEBUG)

def message_handler(message):
    print(message)

my_client = Client()
my_client.start()

my_client.agg_trade(
    symbol="btcusdt",
    id=1,
    callback=message_handler,
)

time.sleep(2)

my_client.agg_trade(
    symbol="ethusdt",
    id=1,
    callback=message_handler,
)

logging.debug("closing ws connection")
my_client.stop()
