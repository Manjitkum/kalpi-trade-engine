from abc import ABC, abstractmethod

class BrokerInterface(ABC):

    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def get_holdings(self):
        pass

    @abstractmethod
    def place_order(self, symbol: str, quantity: int, side: str):
        pass
