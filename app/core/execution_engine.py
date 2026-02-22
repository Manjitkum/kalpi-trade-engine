class ExecutionEngine:

    def __init__(self, broker):
        self.broker = broker

    def execute(self, instructions):
        self.broker.authenticate()
        results = []

        for trade in instructions:
            result = self.broker.place_order(
                trade.symbol,
                trade.quantity,
                trade.side
            )
            results.append(result)

        return results
