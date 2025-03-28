import logging
from aster.rest_api import Client
from aster.lib.utils import config_logging
from aster.error import ClientError

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret, base_url="https://fapi.asterdex.com")

try:
    response = client.cancel_batch_order(symbol = "BTCUSDT", orderIdList=[1234567,2345678], origClientOrderIdList=[1234567,2345678], recvWindow=2000)
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )