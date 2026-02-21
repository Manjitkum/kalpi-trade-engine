class ExecutionEngine:

    def __init__(self, broker):
        self.broker = broker

    def execute(self, target_portfolio: dict):
        self.broker.authenticate()
        current_holdings = self.broker.get_holdings()

        orders = []

        for symbol, target_qty in target_portfolio.items():
            current_qty = current_holdings.get(symbol, 0)

            if target_qty > current_qty:
                diff = target_qty - current_qty
                orders.append(("BUY", symbol, diff))

            elif target_qty < current_qty:
                diff = current_qty - target_qty
                orders.append(("SELL", symbol, diff))

        results = []
        for side, symbol, qty in orders:
            result = self.broker.place_order(symbol, qty, side)
            results.append(result)

        return results
