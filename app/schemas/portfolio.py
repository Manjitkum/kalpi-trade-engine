from pydantic import BaseModel
from typing import List
from app.schemas.trade import Trade


class PortfolioExecutionRequest(BaseModel):
    broker: str
    trades: List[Trade]
