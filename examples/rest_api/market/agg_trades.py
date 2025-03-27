import logging
from aster.rest_api import Client
from aster.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

client = Client()
logging.info(client.agg_trades("BTCUSDT"))







