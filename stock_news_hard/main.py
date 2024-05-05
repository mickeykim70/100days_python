import requests
from appier import api
from newsapi import NewsApiClient



STOCK = 'TSLA'
COMPANY_NAME = 'Tesla Inc'
STOCK_API_KEY = '5H988QQWKJGNE52O'    # https://www.alphavantage.co/
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


#### TEST CODES

#
# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=API_Key'
# r = requests.get(url)
# data = r.json()
#
# print(data)



## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday
# then print("Get News").

# Init
newsapi = NewsApiClient(api_key='113cb5dfe9214e26845aaa996462dc5d')


url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=113cb5dfe9214e26845aaa996462dc5d')
response = requests.get(url)
print(response.json())

#HINT 1: Get the closing price for yesterday and the day before yesterday.
# Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are 
required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of 
March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are 
required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of
 March 31st, near the height of the coronavirus market crash.
"""

