from typing import Optional 
from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import datetime 


class FinData(BaseModel):
    id: Optional[UUID] = uuid4
    name: str
    time: datetime
    open: float
    close: float
    high: float
    low:float