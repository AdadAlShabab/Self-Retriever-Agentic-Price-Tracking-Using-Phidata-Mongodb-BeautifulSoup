from datetime import datetime
from pydantic import BaseModel

class ProductBase(BaseModel):
    product_id: str
    name: str
    url: str
    created_at: datetime = datetime.utcnow()

class PriceHistoryBase(BaseModel):
    product_id: str
    price: float
    recorded_at: datetime = datetime.utcnow()