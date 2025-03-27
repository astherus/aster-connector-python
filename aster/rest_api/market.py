from aster.lib.utils import check_required_parameter
from aster.lib.utils import check_required_parameters


def ping(self):
    """
    |
    | **Test Connectivity**
    | *Test connectivity to the Rest API.*

    :API endpoint: ``GET /fapi/v1/ping``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#test-connectivity
    |
    """

    url_path = "/fapi/v1/ping"
    return self.query(url_path)


def time(self):
    """
    |
    | **Check Server Time**
    | *Test connectivity to the Rest API and get the current server time.*

    :API endpoint: ``GET /fapi/v1/time``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#check-server-time
    |
    """

    url_path = "/fapi/v1/time"
    return self.query(url_path)


def exchange_info(self):
    """
    |
    | **Exchange Information**
    | *Current exchange trading rules and symbol information.*

    :API endpoint: ``GET /fapi/v1/exchangeInfo``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#exchange-information
    |
    """

    url_path = "/fapi/v1/exchangeInfo"
    return self.query(url_path)


def depth(self, symbol: str, **kwargs):
    """
    |
    | **Order Book**

    :API endpoint: ``GET /fapi/v1/depth``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#order-book
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    url_path = "/fapi/v1/depth"
    return self.query(url_path, params)


def trades(self, symbol: str, **kwargs):
    """
    |
    | **Recent Trades List**
    | *Get recent market trades*

    :API endpoint: ``GET /fapi/v1/trades``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#recent-trades-list
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    url_path = "/fapi/v1/trades"
    return self.query(url_path, params)


def historical_trades(self, symbol: str, **kwargs):
    """
    |
    | **Old Trade Lookup (MARKET_DATA)**
    | *Get older market historical trades.*

    :API endpoint: ``GET /fapi/v1/historicalTrades``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#old-trades-lookup-market_data
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    url_path = "/fapi/v1/historicalTrades"
    return self.limit_request("GET", url_path, params)


def agg_trades(self, symbol: str, **kwargs):
    """
    |
    | **Compressed/Aggregate Trades List**
    | *Get compressed, aggregate market trades. Market trades that fill at the time, from the same order, with the same price will have the quantity aggregated.*
    
    :API endpoint: ``GET /fapi/v1/aggTrades``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#compressedaggregate-trades-list
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    url_path = "/fapi/v1/aggTrades"
    return self.query(url_path, params)


def klines(self, symbol: str, interval: str, **kwargs):
    """
    |
    | **Kline/Candlestick Data**
    | *Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.*

    :API endpoint: ``GET /fapi/v1/klines``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#klinecandlestick-data
    |
    """

    check_required_parameters([[symbol, "symbol"], [interval, "interval"]])
    params = {"symbol": symbol, "interval": interval, **kwargs}
    url_path = "/fapi/v1/klines"
    return self.query(url_path, params)


def index_price_klines(self, pair: str, interval: str, **kwargs):
    """
    |
    | **Index Price Kline/Candlestick Data**
    | *Kline/Candlestick Data for the index price of a pair.*
    | *Klines are uniquely identified by their open time.*   
    
    :API endpoint: ``GET /fapi/v1/indexPriceKlines``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#index-price-klinecandlestick-data
    |
    """

    check_required_parameters([[pair, "pair"], [interval, "interval"]])
    params = {"pair": pair, "interval": interval, **kwargs}
    url_path = "/fapi/v1/indexPriceKlines"
    return self.query(url_path, params)


def mark_price_klines(self, symbol: str, interval: str, **kwargs):
    """
    |
    | **Mark Price Kline/Candlestick Data**
    | *Kline/candlestick bars for the mark price of a symbol.*
    | *Klines are uniquely identified by their open time.*
    
    :API endpoint: ``GET /fapi/v1/markPriceKlines``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#mark-price-klinecandlestick-data
    |
    """

    check_required_parameters([[symbol, "symbol"], [interval, "interval"]])
    params = {"symbol": symbol, "interval": interval, **kwargs}
    url_path = "/fapi/v1/markPriceKlines"
    return self.query(url_path, params)


def mark_price(self, symbol: str = None):
    """
    |
    | **Mark Price**
    | *Mark Price and Funding Rate*

    :API endpoint: ``GET /fapi/v1/premiumIndex``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#mark-price
    |
    """

    params = {"symbol": symbol}
    url_path = "/fapi/v1/premiumIndex"
    return self.query(url_path, params)


def funding_rate(self, symbol: str = None,  **kwargs):
    """
    |
    | **Get Funding Rate History**

    :API endpoint: ``GET /fapi/v1/fundingRate``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#get-funding-rate-history
    |
    """
    
    params = {"symbol": symbol, **kwargs}
    url_path = "/fapi/v1/fundingRate"
    return self.query(url_path, params)


def ticker_24hr_price_change(self, symbol: str = None):
    """
    |
    | **24hr Ticker Price Change Statistics**
    | *24 hour rolling window price change statistics.*
    | *Careful when accessing this with no symbol. If the symbol is not sent, tickers for all symbols will be returned in an array.*

    :API endpoint: ``GET /fapi/v1/ticker/24hr``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#24hr-ticker-price-change-statistics
    |
    """

    params = {"symbol": symbol}
    url_path = "/fapi/v1/ticker/24hr"
    return self.query(url_path, params)


def ticker_price(self, symbol: str = None):
    """
    |
    | **Symbol Price Ticker**
    | *Latest price for a symbol or symbols.*
    | *If the symbol is not sent, prices for all symbols will be returned in an array.*

    :API endpoint: ``GET /fapi/v1/ticker/price``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#symbol-price-ticker
    |
    """

    params = {"symbol": symbol}
    url_path = "/fapi/v1/ticker/price"
    return self.query(url_path, params)


def book_ticker(self, symbol: str = None):
    """
    |
    | **Symbol Order Book Ticker**
    | *Best price/qty on the order book for a symbol or symbols.*
    | *If the symbol is not sent, prices for all symbols will be returned in an array.*

    :API endpoint: ``GET /fapi/v1/ticker/bookTicker``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#symbol-order-book-ticker
    |
    """

    params = {"symbol": symbol}
    url_path = "/fapi/v1/ticker/bookTicker"
    return self.query(url_path, params)
