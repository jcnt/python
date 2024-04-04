import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

with open("stock.token") as file: 
    stock_token = file.readline().rstrip()

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_token,
}

stock_result = requests.get(url=STOCK_ENDPOINT, params=stock_params, verify=False)
stock = stock_result.json()["Time Series (Daily)"]
#print(stock['Time Series (Daily)']['2024-04-03']['4. close'])

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. 
# e.g. [new_value for (key, value) in dictionary.items()]

stocklist = [value for (key, value) in stock.items()]
yesterday_close = float(stocklist[0]['4. close'])

#TODO 2. - Get the day before yesterday's closing stock price

dby_close = float(stocklist[1]['4. close'])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

diff_days = abs (yesterday_close - dby_close)
print(diff_days)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

pct_change = (diff_days / yesterday_close) * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

with open("newsapi.token") as file: 
    news_token = file.readline().rstrip()

news_params = {
    "apiKey": news_token,
    "q": COMPANY_NAME,
    "language": "en"
}

if pct_change > 1: 
    

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.


    news_result = requests.get(url=NEWS_ENDPOINT, params=news_params, verify=False)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    news = news_result.json()["articles"][0:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    news_simple = [f"Headline: {article['title']},\n Brief: {article['description']}" for article in news ]
# -> how this works: 
# item for item in list: 
# list is the news we get from API
# there are 3 items in that list, we call them "article"
# we need the article.something and article.something for every article

    for i in news_simple: 
        print(i)


#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

