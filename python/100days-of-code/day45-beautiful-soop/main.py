from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news", verify=False)

ycweb = response.text

soup = BeautifulSoup(ycweb, "html.parser")

article_tag = soup.find(name="a")
article_text = article_tag.getText()
print(article_text)

# 
# This is the Beautiful Soup intro with examples: 
#
#
#
#with open("python/100days-of-code/day45-beautiful-soop/website.html") as file: 
#    content = file.read()
#
#soup = BeautifulSoup(content, "html.parser")
#
#print(soup.title.string)
#print(soup.prettify())
#print("------------")
#
#all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)
#print("------------")
#
#for i in all_anchor_tags:
#    print(i.getText())
#print("------------")
#
#heading = soup.find(name="h1", id="name")
#print(heading)