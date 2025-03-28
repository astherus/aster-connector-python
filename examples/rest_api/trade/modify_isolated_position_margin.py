import logging
from aster.rest_api import Client
from aster.lib.utils import config_logging
from aster.error import ClientError

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret,base_url="https://fapi.asterdex.com")
try:
    response = client.modify_isolated_position_margin(symbol='BTCUSDT', amount = 100, type = 1, recvWindow=6000)
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )