import datetime
import random

with open("quotes.txt", "r") as file: 
    quotes = file.read().split("\n")

randquote = quotes[random.randint(0, len(quotes))]

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

today = datetime.datetime.now()
day = today.weekday()

if weekdays[day] == "Saturday": 
    print(randquote)


