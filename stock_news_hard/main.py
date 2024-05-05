import requests
from appier import api
from newsapi import NewsApiClient

STOCK = 'TSLA'
COMPANY_NAME = 'Tesla Inc'
STOCK_API_KEY = '5H988QQWKJGNE52O'    # https://www.alphavantage.co/
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = '113cb5dfe9214e26845aaa996462dc5d'


# Request alphavantage to get data

alphavantage_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY,
}

# YESTERDAY: getting closing price
response = requests.get(STOCK_ENDPOINT, params=alphavantage_params)
data = response.json()["Time Series (Daily)"]


data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

# DAY BEFORE YESTERDAY: getting closing price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# GAP between days
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
diff_percent = (difference / float(day_before_yesterday_closing_price)) * 100

# Getting NEWS // 3 articles
if diff_percent > 0.1:
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']

    # Select first 3 articles
    three_articles = articles[:3]


    # Headline: {article title} \n Brief: {article description}
    formatted_articles = [f"Headline: {article['title']} \nBrief: {article ['description']}" for article in three_articles]

    for article in formatted_articles:
        print(articles)