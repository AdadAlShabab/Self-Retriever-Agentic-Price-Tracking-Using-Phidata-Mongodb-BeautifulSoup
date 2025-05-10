from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class MongoDB:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGODB_URI"))
        self.db = self.client["price_tracker"]
        self.products = self.db["products"]
        self.price_history = self.db["price_history"]
    
    def get_collection(self, name):
        return self.db[name]