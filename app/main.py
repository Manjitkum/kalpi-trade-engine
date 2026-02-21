from fastapi import FastAPI
from app.brokers.zerodha import ZerodhaBroker
from app.execution.engine import ExecutionEngine

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Kalpi Trade Engine Running"}

@app.post("/execute")
def execute_trades():
    broker = ZerodhaBroker()
    engine = ExecutionEngine(broker)

    target_portfolio = {
        "RELIANCE": 10,
        "INFY": 1
    }

    result = engine.execute(target_portfolio)
    return {"orders": result}
