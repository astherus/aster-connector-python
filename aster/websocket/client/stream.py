from aster.websocket.websocket_client import AsterWebsocketClient


class WebsocketClient(AsterWebsocketClient):
    def __init__(self, stream_url="wss://fstream.asterdex.com"):
        super().__init__(stream_url)

    def agg_trade(self, symbol: str, id: int, callback, **kwargs):
        """
        | **Aggregate Trade Stream**
        | *The Aggregate Trade Streams push market trade information that is aggregated for a single taker order every 100 milliseconds.*
        
        :Stream name: ``<symbol>@aggTrade``
        :Doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#aggregate-trade-streams
        """

        self.live_subscribe(
            "{}@aggTrade".format(symbol.lower()), id, callback, **kwargs
        )

    def mark_price(self, symbol: str, id: int, callback, speed=None, **kwargs):
        """
        | **Mark Price Stream**
        | *Mark price and funding rate for a single symbol pushed every 3 seconds or every second.*
        
        :Stream name: ``<symbol>@markPrice`` or ``<symbol>@markPrice@1s``
        :Doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#mark-price-stream
        """

        if speed is None:
            self.live_subscribe(
                "{}@markPrice".format(symbol.lower()), id, callback, **kwargs
            )
        else:
            self.live_subscribe(
                "{}@markPrice@{}s".format(symbol.lower(), speed), id, callback, **kwargs
            )

    def mark_price_all_market(self, id: int, callback, speed=None, **kwargs):
        """
        | **Mark Price Stream for All market**
        | *Mark price and funding rate for all symbols pushed every 3 seconds or every second.*
        
        :Stream name: ``!markPrice@arr`` or ``!markPrice@arr@1s``
        :Doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#mark-price-stream-for-all-market
        """
        if speed is None:
            self.live_subscribe("{!markPrice@arr", id, callback, **kwargs)
        else:
            self.live_subscribe(
                "{!markPrice@arr@{}s".format(speed), id, callback, **kwargs
            )

    def kline(self, symbol: str, id: int, interval: str, callback, **kwargs):
        """
        | **Kline/Candlestick Streams**
        | *The Kline/Candlestick Stream push updates to the current klines/candlestick every 250 milliseconds (if existing).*
        
        :Stream name: ``<symbol>@kline_<interval>``
        :Doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#klinecandlestick-streams
        """

        self.live_subscribe(
            "{}@kline_{}".format(symbol.lower(), interval), id, callback, **kwargs
        )      

    def mini_ticker(self, id: int, callback, symbol=None, **kwargs):
        """
        | **Individual Symbol or All Market Mini Ticker Stream**
        | *24hr rolling window mini-ticker statistics for a single symbol or all market. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.*
        
        :Stream name: ``<symbol>@miniTicker``
        :Stream name: ``!miniTicker@arr``
        :Doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#individual-symbol-mini-ticker-stream
        :Doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#all-market-mini-tickers-stream
        """

        if symbol is None:
            self.live_subscribe("!miniTicker@arr", id, callback, **kwargs)
        else:
            self.live_subscribe(
                "{}@miniTicker".format(symbol.lower()), id, callback, **kwargs
            )

    def ticker(self, id: int, callback, symbol=None, **kwargs):
        """
        | **Individual Symbol or All Market Ticker Streams**
        | *24hr rollwing window ticker statistics for a single symbol or all market. These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.*
        
        :Stream name: ``<symbol>@ticker``
        :Stream name: ``!ticker@arr``
        :Doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#individual-symbol-ticker-streams
        :Doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#all-market-tickers-streams
        """

        if symbol is None:
            self.live_subscribe("!ticker@arr", id, callback, **kwargs)
        else:
            self.live_subscribe(
                "{}@ticker".format(symbol.lower()), id, callback, **kwargs
            )

    def book_ticker(self, id: int, callback, symbol=None, **kwargs):
        """
        | **Individual Symbol or All Market Book Ticker Streams**
        | *Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol or all market.*
        
        :Stream name: ``<symbol>@bookTicker``
        :Stream name: ``!bookTicker``
        :Doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#individual-symbol-book-ticker-streams
        :Doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#all-book-tickers-stream
        """

        if symbol is None:
            self.live_subscribe("!bookTicker", id, callback, **kwargs)
        else:
            self.live_subscribe(
                "{}@bookTicker".format(symbol.lower()), id, callback, **kwargs
            )

    def liquidation_order(self, id: int, callback, symbol=None, **kwargs):
        """
        | **Liquidation Order Streams**
        | *The Liquidation Order Snapshot Streams push force liquidation order information for specific symbol or all market.*
        
        :Stream name: ``<symbol>@forceOrder``
        :Stream name: ``!forceOrder@arr``
        :Doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#liquidation-order-streams
        :Doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#all-market-liquidation-order-streams
        """

        if symbol is None:
            self.live_subscribe("!forceOrder@arr", id, callback, **kwargs)
        else:
            self.live_subscribe(
                "{}@forceOrder".format(symbol.lower()), id, callback, **kwargs
            )

    def partial_book_depth(self, symbol: str, id: int, level, speed, callback, **kwargs):
        """
        | **Partial Book Depth Streams**
        | *Top <levels> bids and asks, Valid <levels> are 5, 10, or 20. Valid <speed> are 250, 500, or 100*
        
        :Stream name: ``<symbol>@depth<levels>`` or ``<symbol>@depth<levels>@500ms`` or ``<symbol>@depth<levels>@100ms``
        :Doc: https://github.com/astherus/api-docss/blob/master/aster-finance-api.md#partial-book-depth-streams
        """

        self.live_subscribe(
            "{}@depth{}@{}ms".format(symbol.lower(), level, speed), id, callback, **kwargs
        )

    def diff_book_depth(self, symbol: str, id: int, speed, callback, **kwargs):
        """
        | **Diff. Book Depth Streams**
        | *Bids and asks, pushed every 250 milliseconds, 500 milliseconds, 100 milliseconds (if existing)*
        
        :Stream name: ``<symbol>@depth`` or ``<symbol>@depth@500ms`` or ``<symbol>@depth@100ms``
        :Doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#diff-book-depth-streams
        """

        self.live_subscribe(
            "{}@depth@{}ms".format(symbol.lower(), speed), id, callback, **kwargs
        )

    def user_data(self, listen_key: str, id: int, callback, **kwargs):
        """listen to user data by provided listenkey"""
        self.live_subscribe(listen_key, id, callback, **kwargs)