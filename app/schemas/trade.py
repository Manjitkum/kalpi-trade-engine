from pydantic import BaseModel
from typing import List


class Trade(BaseModel):
    symbol: str
    quantity: int
    side: str
