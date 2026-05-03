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
    #2 levels of error: network error + api error
    #network error e.g. request time out, connection error -> wrap requests.get() inside try/except
    #api error -> need another handling
    try:
        #Step 1: Get response from api
        response = requests.get(f"https://newsapi.org/v2/everything?q={topic}&sources=bbc-news&apiKey={news_api_key}")
        #want to restrict to english, cant use language and sources together
        content = response.json()
    except Exception as e:
        print(f"Network Error: {e}")
        return None #return None is no article is found

    #Here the response has sth, no network error, check returned object is correct
    if content["status"] != "ok":
        return print(f"code: {content.get("code", "unknown code")}, message: {content.get("message", "unknown error")}")

    return content.get("articles", [])

    
    

