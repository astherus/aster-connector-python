#!/usr/bin/env python
import logging
from aster.rest_api import Client
from aster.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""

client = Client(key, base_url="https://fapi.asterdex.com")
logging.info(client.new_listen_key())
