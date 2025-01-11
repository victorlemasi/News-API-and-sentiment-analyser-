Python script integrates Bing News Search API, Hugging Face Transformers, and MetaTrader 5 (MT5) to automate trading decisions based on news sentiment analysis. Here's a summary of its components:

1. Fetching News from Bing News API
Purpose: Retrieves the latest news articles about a specific topic (e.g., "stock market").
Key Function:
get_news(query, market, count) sends a request to the Bing News API with a query (search term) and returns the top news articles.
Customization: Replace BING_API_KEY with your Bing API key.
2. Sentiment Analysis with Hugging Face Transformers
Purpose: Analyzes the sentiment (positive or negative) of news articles.
Key Function:
analyze_sentiment(news_content) uses a pre-trained NLP model to classify news sentiment as "POSITIVE" or "NEGATIVE" with a confidence score.
Logic:
Sentiment and score are used to determine trading actions:
"POSITIVE" with a high score (> 0.8) triggers a buy order.
"NEGATIVE" with a high score (> 0.8) triggers a sell order.
3. MetaTrader 5 (MT5) Integration
Purpose: Connects to the MT5 platform to execute buy/sell orders based on news sentiment.
Key Functions:
initialize_mt5(login_id, password, server):
Initializes MT5, logs into the trading account, and prints account details.
place_order(action, symbol, volume):
Places a buy or sell order for a specified symbol (default: "EURUSD") with a defined volume (default: 0.1).
mt5.shutdown() closes the connection to MT5.
4. Workflow
The script performs the following steps:
Fetches news articles about the query topic (e.g., "stock market").
Analyzes the sentiment of each news article's title or description.
Logs into the MT5 platform using user credentials.
Places buy/sell orders based on the sentiment analysis results.
Disconnects from MT5 after processing.
5. Requirements
Bing News API: Provides the latest news articles.
Hugging Face Transformers: Performs sentiment analysis using NLP.
MetaTrader 5: Executes trades based on the sentiment.
Python Libraries: requests, transformers, MetaTrader5, and pandas.
Summary of Trading Logic
Positive News: Buy.
Negative News: Sell.
Neutral or Low-Confidence News: Hold.
This script automates news-driven trading strategies, leveraging sentiment analysis and MT5 trading capabilities
