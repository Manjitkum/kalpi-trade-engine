from app.brokers.base import BrokerInterface


class GrowwBroker(BrokerInterface):

    def authenticate(self):
        return True

    def get_holdings(self):
        return {}

    def place_order(self, symbol, quantity, side):
        return {
            "broker": "Groww",
            "symbol": symbol,
            "quantity": quantity,
            "side": side,
            "status": "success"
        }
