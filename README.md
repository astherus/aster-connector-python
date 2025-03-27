# aster-connector-python

[![Python 3.6](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a lightweight library that works as a connector to [Aster Finance public API](https://github.com/astherus/api-docs)

## Installation

```bash
pip install aster-connector-python
```

## Documentation


## RESTful APIs

Usage examples:
```python
from aster.rest_api import Client 

# Get timestamp
client = Client()
print(client.time())


client = Client(key='<api_key>', secret='<api_secret>')

# Get account information
print(client.account())

# Post a new order
params = {
    'symbol': 'BTCUSDT',
    'side': 'SELL',
    'type': 'LIMIT',
    'timeInForce': 'GTC',
    'quantity': 0.002,
    'price': 59808
}

response = client.new_order(**params)
print(response)
```
Please find `examples` folder to check for more endpoints.

### Base URL
`https://fapi.astherus.finance`

### Optional parameters

PEP8 suggests _lowercase with words separated by underscores_, but for this connector,
the methods' optional parameters should follow their exact naming as in the API documentation.

```python
# Recognised parameter name
response = client.query_order('BTCUSDT', orderListId=1)

# Unrecognised parameter name
response = client.query_order('BTCUSDT', order_list_id=1)
```

### RecvWindow parameter

Additional parameter `recvWindow` is available for endpoints requiring signature.<br/>
It defaults to `5000` (milliseconds) and can be any value lower than `60000`(milliseconds).
Anything beyond the limit will result in an error response from aster server.

```python
from aster.rest_api import Client

client = Client(key, secret)
response = client.query_order('BTCUSDT', orderId=11, recvWindow=10000)
```

### Timeout

`timeout` is available to be assigned with the number of seconds you find most appropriate to wait for a server response.<br/>
Please remember the value as it won't be shown in error message _no bytes have been received on the underlying socket for timeout seconds_.<br/>
By default, `timeout` is None. Hence, requests do not time out.

```python
from aster.rest_api import Client

client= Client(timeout=1)
```

### Proxy
proxy is supported

```python
from aster.rest_api import Client

proxies = { 'https': 'http://1.2.3.4:8080' }

client= Client(proxies=proxies)
```

### Response Metadata

The aster API server provides weight usages in the headers of each response.
You can display them by initializing the client with `show_limit_usage=True`:

```python
from aster.rest_api import Client

client = Client(show_limit_usage=True)
print(client.time())
```

You can also display full response metadata to help in debugging:

```python
client = Client(show_header=True)
print(client.time())
```

If `ClientError` is received, it'll display full response meta information.

### Display logs

Setting the log level to `DEBUG` will log the request URL, payload and response text.

### Error

There are 2 types of error returned from the library:
- `aster.error.ClientError`
    - This is thrown when server returns `4XX`, it's an issue from client side.
    - It has 4 properties:
        - `status_code` - HTTP status code
        - `error_code` - Server's error code, e.g. `-1102`
        - `error_message` - Server's error message, e.g. `Unknown order sent.`
        - `header` - Full response header. 
- `aster.error.ServerError`
    - This is thrown when server returns `5XX`, it's an issue from server side.

## Websocket

```python
from aster.websocket.client.stream import WebsocketClient as Client

def message_handler(message):
    print(message)

ws_client = Client()
ws_client.start()

ws_client.mini_ticker(
    symbol='bnbusdt',
    id=1,
    callback=message_handler,
)

# Combine selected streams
ws_client.instant_subscribe(
    stream=['bnbusdt@bookTicker', 'ethusdt@bookTicker'],
    callback=message_handler,
)

ws_client.stop()
```
More websocket examples are available in the `examples` folder

### Heartbeat

Once connected, the websocket server sends a ping frame every 3 minutes and requires a response pong frame back within
a 10 minutes period. This package handles the pong responses automatically.

