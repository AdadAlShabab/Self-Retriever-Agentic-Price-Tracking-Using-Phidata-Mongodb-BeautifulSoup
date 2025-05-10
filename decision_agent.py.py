from phidata.agent.base import Agent
from phidata.llm.openai import OpenAIChat
from phidata.tools import Toolkit
from typing import List, Dict

class PriceDecisionAgent(Agent):
    def __init__(self):
        super().__init__(
            llm=OpenAIChat(model="gpt-4"),
            tools=[PriceAnalysisTool()],
            system_prompt="You are an expert ecommerce price analyst. Provide clear purchase recommendations based on historical pricing data."
        )

class PriceAnalysisTool(Toolkit):
    def analyze_prices(self, price_data: List[Dict]):
        """Analyze price trends and provide recommendations"""
        current_price = price_data[-1]['price']
        min_price = min(p['price'] for p in price_data)
        
        recommendation = "Consider buying now" if current_price <= min_price \
            else "Wait for better price"
        
        analysis = {
            "current_price": current_price,
            "7_day_min": min_price,
            "recommendation": recommendation
        }
        return analysis