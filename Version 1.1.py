import requests
import MetaTrader5 as mt5
from transformers import pipeline
import pandas as pd

# 1. Bing News API Setup
BING_API_KEY = "your_bing_api_key"  # Replace with your Bing News API key
BING_NEWS_URL = "https://api.bing.microsoft.com/v7.0/news/search"

def get_news(query, market="en-US", count=5):
    headers = {"Ocp-Apim-Subscription-Key": BING_API_KEY}
    params = {"q": query, "mkt": market, "count": count}
    response = requests.get(BING_NEWS_URL, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get("value", [])
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []

# 2. Sentiment Analysis
# Load a pre-trained sentiment-analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(news_content):
    result = sentiment_analyzer(news_content)
    return result[0]["label"], result[0]["score"]

# 3. MetaTrader 5 Setup
def initialize_mt5():
    if not mt5.initialize():
        print("MetaTrader5 initialization failed")
        return False
    print("MetaTrader5 initialized")
    return True

def place_order(action, symbol="EURUSD", volume=0.1):
    # Create an order dictionary
    order = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": mt5.ORDER_TYPE_BUY if action == "buy" else mt5.ORDER_TYPE_SELL,
        "price": mt5.symbol_info_tick(symbol).ask if action == "buy" else mt5.symbol_info_tick(symbol).bid,
        "deviation": 20,
        "magic": 234000,
        "comment": "Automated trading",
    }
    # Send the order to MetaTrader 5
    result = mt5.order_send(order)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Order failed: {result.comment}")
    else:
        print(f"Order successful: {action}")

# 4. Main Workflow
if __name__ == "__main__":
    query = "stock market"  # Replace with your desired topic
    news_articles = get_news(query)

    if initialize_mt5():
        for news in news_articles:
            print(f"Title: {news['name']}")
            print(f"Description: {news['description']}")
            print(f"URL: {news['url']}")

            sentiment, score = analyze_sentiment(news['description'] or news['name'])
            print(f"Sentiment: {sentiment}, Score: {score}")

            # Decision-making based on sentiment
            if sentiment == "POSITIVE" and score > 0.8:
                print("Decision: Buy")
                place_order("buy")
            elif sentiment == "NEGATIVE" and score > 0.8:
                print("Decision: Sell")
                place_order("sell")
            else:
                print("Decision: Hold")

        mt5.shutdown()
