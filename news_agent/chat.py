# this script is only responsible for sending message to model, then fetching response, nothing else
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")


def chat(messages):
    #call api
    client = OpenAI(
    api_key=deepseek_api_key,
    base_url="https://api.deepseek.com"
    )

    response = client.chat.completions.create(
        model="deepseek-chat",  # or deepseek-reasoner
        messages=messages
    )
    #return reply string
    return response.choices[0].message.content

#test_messages = [{"role": "user", "content": "hello!"}]
#print(chat(test_messages))