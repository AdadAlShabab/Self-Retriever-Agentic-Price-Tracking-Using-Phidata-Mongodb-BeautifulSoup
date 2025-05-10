from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from src.database.models import PriceHistory

class PriceAnalyzer:
    def __init__(self, db_url):
        engine = create_engine(db_url)
        Session = sessionmaker(bind=engine)
        self.session = Session()
    
    def get_price_trend(self, product_id):
        seven_days_ago = datetime.now() - timedelta(days=7)
        prices = self.session.query(PriceHistory).filter(
            PriceHistory.product_id == product_id,
            PriceHistory.recorded_at >= seven_days_ago
        ).order_by(PriceHistory.recorded_at).all()
        
        if len(prices) < 2:
            return "insufficient_data"
        
        current_price = prices[-1].price
        average_price = sum(p.price for p in prices) / len(prices)
        
        if current_price < average_price:
            return "below_average"
        else:
            return "above_average"