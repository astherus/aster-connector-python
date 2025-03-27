from aster.lib.utils import check_required_parameter
from aster.lib.utils import check_required_parameters


def change_position_mode(self, dualSidePosition: str, **kwargs):
    """
    |
    | **Change Position Mode (TRADE)**
    | *Change user's position mode (Hedge Mode or One-way Mode) on EVERY symbol*

    :API endpoint: ``POST /fapi/v1/positionSide/dual``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#change-position-modetrade
    |
    """

    check_required_parameter(dualSidePosition, "dualSidePosition")
    params = {"dualSidePosition": dualSidePosition, **kwargs}
    url_path = "/fapi/v1/positionSide/dual"
    return self.sign_request("POST", url_path, params)


def get_position_mode(self, **kwargs):
    """
    |
    | **Get Current Position Mode (USER_DATA)**
    | *Get user's position mode (Hedge Mode or One-way Mode) on EVERY symbol*

    :API endpoint: ``GET /fapi/v1/positionSide/dual``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#get-current-position-modeuser_data
    |
    """

    params = {**kwargs}
    url_path = "/fapi/v1/positionSide/dual"
    return self.sign_request("GET", url_path, params)


def change_multi_asset_mode(self, multiAssetsMargin: str, **kwargs):
    """
    |
    | **Change Multi-Assets Mode (TRADE)**
    | *Change user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol*

    :API endpoint: ``POST /fapi/v1/multiAssetsMargin``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#change-multi-assets-mode-trade
    |
    """

    check_required_parameter(multiAssetsMargin, "multiAssetsMargin")
    params = {"multiAssetsMargin": multiAssetsMargin, **kwargs}
    url_path = "/fapi/v1/multiAssetsMargin"
    return self.sign_request("POST", url_path, params)


def get_multi_asset_mode(self, **kwargs):
    """
    |
    | **Get Current Multi-Assets Mode (USER_DATA)**
    | *Get user's Multi-Assets mode (Multi-Assets Mode or Single-Asset Mode) on Every symbol*

    :API endpoint: ``GET /fapi/v1/multiAssetsMargin``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#get-current-multi-assets-mode-user_data
    |
    """

    params = {**kwargs}
    url_path = "/fapi/v1/multiAssetsMargin"
    return self.sign_request("GET", url_path, params)


def new_order(self, symbol: str, side: str, type: str, **kwargs):
    """
    |
    | **New Order (TRADE)**
    | *Send in a new order.*

    :API endpoint: ``POST /fapi/v1/order``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#new-order--trade
    |
    """

    check_required_parameters([[symbol, "symbol"], [side, "side"], [type, "type"]])
    params = {"symbol": symbol, "side": side, "type": type, **kwargs}
    url_path = "/fapi/v1/order"
    return self.sign_request("POST", url_path, params)


def new_batch_order(self, batchOrders: list):
    """
    |
    | **Place Multiple Orders (TRADE)**

    :API endpoint: ``POST /fapi/v1/batchOrders``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#place-multiple-orders--trade
    |
    """

    params = {"batchOrders": batchOrders}
    url_path = "/fapi/v1/batchOrders"
    return self.sign_request("POST", url_path, params, True)


def query_order(self, symbol: str, orderId: int = None, origClientOrderId: str = None, **kwargs):
    """
    |
    | **Query Order (USER_DATA)**
    | *Check an order's status*
    | *Either orderId or origClientOrderId must be sent.*

    :API endpoint: ``GET /fapi/v1/order``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#query-order-user_data
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    url_path = "/fapi/v1/order"
    return self.sign_request("GET", url_path, params)


def cancel_order(self, symbol: str, orderId: int = None, origClientOrderId: str = None, **kwargs):
    """
    |
    | **Cancel Order (TRADE)**
    | *Cancel an active order.*
    | *Either orderId or origClientOrderId must be sent.*

    :API endpoint: ``DELETE /fapi/v1/order``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#cancel-order-trade
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    url_path = "/fapi/v1/order"
    return self.sign_request("DELETE", url_path, params)


def cancel_open_orders(self, symbol: str, **kwargs):
    """
    |
    | **Cancel All Open Orders (TRADE)**

    :API endpoint: ``DELETE /fapi/v1/allOpenOrders``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#cancel-all-open-orders-trade
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    url_path = "/fapi/v1/allOpenOrders"
    return self.sign_request("DELETE", url_path, params)


def cancel_batch_order(self, symbol: str, orderIdList: list, origClientOrderIdList: list, **kwargs):
    """
    |
    | **Cancel Multiple Orders (TRADE)**
    | *Either orderIdList or origClientOrderIdList must be sent.*

    :API endpoint: ``DELETE /fapi/v1/batchOrders``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#cancel-multiple-orders-trade
    |
    """
    
    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    url_path = "/fapi/v1/batchOrders"
    return self.sign_request("DELETE", url_path, params)


def countdown_cancel_order(self, symbol: str, countdownTime: int, **kwargs):
    """
    |
    | **Auto-Cancel All Open Orders (TRADE)**
    | *Cancel all open orders of the specified symbol at the end of the specified countdown.*

    :API endpoint: ``POST /fapi/v1/countdownCancelAll``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#auto-cancel-all-open-orders-trade
    |
    """
    
    check_required_parameters([[symbol, "symbol"], [countdownTime, "countdownTime"]])
    params = {"symbol": symbol, "countdownTime": countdownTime, **kwargs}
    url_path = "/fapi/v1/countdownCancelAll"
    return self.sign_request("POST", url_path, params)


def get_open_orders(self, symbol: str, orderId: int = None, origClientOrderId: str = None, **kwargs):
    """
    |
    | **Query Current Open Order (USER_DATA)**
    | *EitherorderId or origClientOrderId must be sent.*

    :API endpoint: ``GET /fapi/v1/openOrder``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#query-current-open-order-user_data
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    url_path = "/fapi/v1/openOrder"
    return self.sign_request("GET", url_path, params)


def get_orders(self, **kwargs):
    """
    |
    | **Current All Open Orders (USER_DATA)**
    | *Get all open orders on a symbol. Careful when accessing this with no symbol.*
    | *If the symbol is not sent, orders for all symbols will be returned in an array.*

    :API endpoint: ``GET /fapi/v1/openOrders``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#current-all-open-orders-user_data
    |
    """

    params = { **kwargs }
    url_path = "/fapi/v1/openOrders"
    return self.sign_request("GET", url_path, params)


def get_all_orders(self, symbol: str, **kwargs):
    """
    |
    | **All Orders (USER_DATA)**
    | *Get all account orders; active, canceled, or filled.*

    :API endpoint: ``GET /fapi/v1/allOrders``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#all-orders-user_data
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    url_path = "/fapi/v1/allOrders"
    return self.sign_request("GET", url_path, params)


def balance(self, **kwargs):
    """
    |
    | **Futures Account Balance V2 (USER_DATA)**

    :API endpoint: ``GET /fapi/v2/balance``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#futures-account-balance-v2-user_data
    |
    """

    url_path = "/fapi/v2/balance"
    return self.sign_request("GET", url_path, {**kwargs})


def account(self, **kwargs):
    """
    |
    | **Account Information V2 (USER_DATA)**
    | *Get current account information. User in single-asset/ multi-assets mode will see different value, see comments in response section for detail.*

    :API endpoint: ``GET /fapi/v2/account``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#account-information-v2-user_data
    |
    """

    url_path = "/fapi/v2/account"
    return self.sign_request("GET", url_path, {**kwargs})


def change_leverage(self, symbol: str, leverage: int, **kwargs):
    """
    |
    | **Change Initial Leverage (TRADE)**
    | *Change user's initial leverage of specific symbol market.*

    :API endpoint: ``POST /fapi/v1/leverage``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#change-initial-leverage-trade
    |
    """

    check_required_parameters([[symbol, "symbol"],[leverage, "leverage"]])
    params = {"symbol": symbol, "leverage":leverage, **kwargs}
    url_path = "/fapi/v1/leverage"
    return self.sign_request("POST", url_path, params)


def change_margin_type(self, symbol: str, marginType: str, **kwargs):
    """
    |
    | **Change margin type (TRADE)**

    :API endpoint: ``POST /fapi/v1/marginType``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#change-margin-type-trade
    |
    """

    check_required_parameters([[symbol, "symbol"],[marginType, "marginType"]])    
    params = {"symbol": symbol, "marginType": marginType, **kwargs}
    url_path = "/fapi/v1/marginType"
    return self.sign_request("POST", url_path, params)


def modify_isolated_position_margin(self, symbol: str, amount: float, type: int, **kwargs):
    """
    |
    | **Modify Isolated Position Margin (TRADE)**

    :API endpoint: ``POST /fapi/v1/positionMargin``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#modify-isolated-position-margin-trade
    |
    """

    check_required_parameters([[symbol, "symbol"], [amount, "amount"], [type, "type"]])
    params = {"symbol": symbol, "amount":amount, "type":type, **kwargs}
    url_path = "/fapi/v1/positionMargin"
    return self.sign_request("POST", url_path, params)


def get_position_margin_history(self, symbol: str, **kwargs):
    """
    |
    | **Get Position Margin Change History (TRADE)**

    :API endpoint: ``GET /fapi/v1/positionMargin/history``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#get-position-margin-change-history-trade
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    url_path = "/fapi/v1/positionMargin/history"
    return self.sign_request("GET", url_path, params)


def get_position_risk(self, **kwargs):
    """
    |
    | **Position Information V2 (USER_DATA)**
    | *Get current position information.*

    :API endpoint: ``GET /fapi/v2/positionRisk``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#position-information-v2-user_data
    |
    """
    params = {**kwargs}
    url_path = "/fapi/v2/positionRisk"
    return self.sign_request("GET", url_path, params)


def get_account_trades(self, symbol: str, **kwargs):
    """
    |
    | **Account Trade List (USER_DATA)**
    | *Get trades for a specific account and symbol.*

    :API endpoint: ``GET /fapi/v1/userTrades``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#account-trade-list-user_data
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    url_path = "/fapi/v1/userTrades"
    return self.sign_request("GET", url_path, params)


def get_income_history(self, **kwargs):
    """
    |
    | **Get Income History (USER_DATA)**

    :API endpoint: ``GET /fapi/v1/income``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#get-income-historyuser_data
    |
    """

    params = {**kwargs}
    url_path = "/fapi/v1/income"
    return self.sign_request("GET", url_path, params)


def leverage_brackets(self, **kwargs):
    """
    |
    | **Notional and Leverage Brackets (USER_DATA)**

    :API endpoint: ``GET /fapi/v1/leverageBracket``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#notional-and-leverage-brackets-user_data
    |
    """

    params = {**kwargs}
    url_path = "/fapi/v1/leverageBracket"
    return self.sign_request("GET", url_path, params)


def adl_quantile(self, **kwargs):
    """
    |
    | **Position ADL Quantile Estimation (USER_DATA)**

    :API endpoint: ``GET /fapi/v1/adlQuantile``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#position-adl-quantile-estimation-user_data
    |
    """

    params = {**kwargs}
    url_path = "/fapi/v1/adlQuantile"
    return self.sign_request("GET", url_path, params)


def force_orders(self, **kwargs):
    """
    |
    | **User's Force Orders (USER_DATA)**

    :API endpoint: ``GET /fapi/v1/forceOrders``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#users-force-orders-user_data
    |
    """

    params = {**kwargs}
    url_path = "/fapi/v1/forceOrders"
    return self.sign_request("GET", url_path, params)


def commission_rate(self, symbol: str, **kwargs):
    """
    |
    | **User Commission Rate (USER_DATA)**

    :API endpoint: ``GET /fapi/v1/commissionRate``
    :API doc: https://github.com/astherus/api-docs/blob/master/aster-finance-api.md#user-commission-rate-user_data
    |
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol":symbol, **kwargs}
    url_path = "/fapi/v1/commissionRate"
    return self.sign_request("GET", url_path, params)
