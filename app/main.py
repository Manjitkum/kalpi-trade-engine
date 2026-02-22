from fastapi import FastAPI
from app.schemas.portfolio import PortfolioExecutionRequest
from app.core.execution_engine import ExecutionEngine
from app.notifications.notifier import Notifier

from app.brokers.zerodha import ZerodhaBroker
from app.brokers.fyers import FyersBroker
from app.brokers.angelone import AngelOneBroker
from app.brokers.groww import GrowwBroker
from app.brokers.upstox import UpstoxBroker

app = FastAPI()


def get_broker(broker_name: str):
    brokers = {
        "zerodha": ZerodhaBroker(),
        "fyers": FyersBroker(),
        "angelone": AngelOneBroker(),
        "groww": GrowwBroker(),
        "upstox": UpstoxBroker()
    }
    return brokers.get(broker_name.lower())


@app.post("/execute")
def execute_portfolio(request: PortfolioExecutionRequest):

    broker = get_broker(request.broker)

    if not broker:
        return {"error": "Unsupported broker"}

    engine = ExecutionEngine(broker)
    results = engine.execute(request.trades)

    notifier = Notifier()
    notifier.notify(results)

    return {"executed_trades": results}
