from .base import BrokerInterface

class ZerodhaBroker(BrokerInterface):

    def authenticate(self):
        print("Zerodha authenticated")
        return True

    def get_holdings(self):
        return {
            "RELIANCE": 5,
            "INFY": 2
        }

    def place_order(self, symbol: str, quantity: int, side: str):
        print(f"{side} {quantity} of {symbol} via Zerodha")
        return {"status": "success", "symbol": symbol, "qty": quantity, "side": side}
