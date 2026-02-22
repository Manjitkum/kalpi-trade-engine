from app.brokers.base import BrokerInterface


class FyersBroker(BrokerInterface):

    def authenticate(self):
        return True

    def get_holdings(self):
        return {"TCS": 3}

    def place_order(self, symbol, quantity, side):
        return {
            "broker": "Fyers",
            "symbol": symbol,
            "quantity": quantity,
            "side": side,
            "status": "success"
        }
