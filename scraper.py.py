import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

class BaseScraper:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {'User-Agent': UserAgent().random}
    
    def fetch_price(self, url):
        raise NotImplementedError("Subclasses must implement fetch_price")