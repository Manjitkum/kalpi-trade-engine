from app.brokers.base import BrokerInterface


class AngelOneBroker(BrokerInterface):

    def authenticate(self):
        return True

    def get_holdings(self):
        return {}

    def place_order(self, symbol, quantity, side):
        return {
            "broker": "AngelOne",
            "symbol": symbol,
            "quantity": quantity,
            "side": side,
            "status": "success"
        }
