from aster.rest_api import Client
import logging
from aster.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

client = Client()
logging.info(client.funding_rate("BTCUSDT",**{'limit':100}))


