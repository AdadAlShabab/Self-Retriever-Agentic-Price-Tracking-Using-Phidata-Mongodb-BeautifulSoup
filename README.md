# Self-Retriever-Price-Tracking-AI-Agent-Using-Phidata-Mongodb-BeautifulSoup

An intelligent system that monitors e-commerce product prices, analyzes historical trends, and provides AI-driven purchase recommendations.

## Features

- **Web Scraping**: Extracts product prices from major e-commerce platforms
- **MongoDB Storage**: Efficiently stores price history and product data
- **Trend Analysis**: Identifies price patterns over 7-day periods
- **AI Recommendations**: GPT-4 powered purchase suggestions
- **PDF Reports**: Generates detailed daily/weekly reports
- **Multi-Store Support**: Extensible architecture for new retailers

## Technologies Used

- **Python 3.10+**
- **MongoDB** (Time-Series Collections)
- **Phidata** (AI Agent Framework)
- **BeautifulSoup** (Web Scraping)
- **Jinja2** & **PDFKit** (Reporting)
- **Pydantic** (Data Validation)

## Installation
```pip install -r requirements.txt```
## Using Docker
```docker run -d -p 27017:27017 --name price-tracker-db mongo:latest```
## Usage
```# Environment Config
cp .env.example .env
# Edit .env file with your credentials

## Configuration (env)
```bash
MONGODB_URI=mongodb://localhost:27017/price_tracker
OPENAI_API_KEY=your_openai_key_here
DB_NAME=price_tracker
LOG_LEVEL=INFO```

## Track Product Price
```from src.scraper.amazon_scraper import AmazonScraper
from src.database.crud import CRUD
from src.database.mongodb import MongoDB

# Initialize components
db = MongoDB()
crud = CRUD(db)
scraper = AmazonScraper()

# Track product
product_url = "https://www.amazon.com/product-example"
price = scraper.fetch_price(product_url)

# Store data
crud.create_price_entry({
    "product_id": "AMZN123",
    "price": price,
    "recorded_at": datetime.utcnow()
})
## Generate Report
```from src.agent.decision_agent import PriceDecisionAgent
from src.report.report_generator import ReportGenerator

agent = PriceDecisionAgent()
report_data = agent.analyze_product("AMZN123")

generator = ReportGenerator()
generator.generate_pdf_report(report_data, "price_report.pdf")

```bash
price-tracker-agent/
├── .env                    # Environment configuration
├── main.py                 # Main application entry
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container configuration
│
├── src/                    # Source code
│   ├── scraper/            # Website scrapers
│   ├── database/           # MongoDB operations
│   ├── analyzer/           # Price analysis logic
│   ├── agent/              # AI decision components
│   ├── report/             # Report generation
│   └── utils/              # Helper functions
│
└── tests/                  # Unit and integration tests
```
### Prerequisites
```
- Python 3.10+
- MongoDB (Local or Atlas Cluster)
- OpenAI API Key
- wkhtmltopdf (for PDF generation)
```
**Clone Repository**
```bash
git clone https://github.com/yourusername/price-tracker-agent.git
cd price-tracker-agent```
