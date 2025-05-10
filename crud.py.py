from datetime import datetime, timedelta
from .schemas import ProductBase, PriceHistoryBase

class CRUD:
    def __init__(self, db):
        self.db = db

    def create_product(self, product: ProductBase):
        return self.db.products.insert_one(product.dict())

    def get_product(self, product_id):
        return self.db.products.find_one({"product_id": product_id})

    def create_price_entry(self, price_data: PriceHistoryBase):
        return self.db.price_history.insert_one(price_data.dict())

    def get_price_history(self, product_id, days=7):
        cutoff_date = datetime.utcnow() - timedelta(days=days)
        return list(self.db.price_history.find({
            "product_id": product_id,
            "recorded_at": {"$gte": cutoff_date}
        }).sort("recorded_at", 1))