import requests
from dotenv import load_dotenv
from openai import OpenAI
import os, json

load_dotenv() #what is this
news_api_key = os.getenv("NEWS_API_KEY")



"""
Umm what need to exist inside this news fetcher script
go to API documentation -> top headlines endpoint
Top headlines about trump
GET https://newsapi.org/v2/top-headlines?q=trump&apiKey=API_KEY

full url
response.get()
parse the returned message
print it out

Next step: display headlines to users and let them pick one
oh yeah can make it a really simple CLI thing first
"""


def get_headlines(topic=None):
    try:
        response = requests.get(f"https://newsapi.org/v2/everything?q={topic}&sources=bbc-news&apiKey={news_api_key}")
        #want to restrict to english, cant use language and sources together
        content = response.json()
        if len(content["articles"]) == 0:
            print("no article found")
        else:
            print(content["articles"][0])
    except Exception as e:
        print(e)
    return content

