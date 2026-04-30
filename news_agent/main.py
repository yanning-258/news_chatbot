"""
return fetched news headline to user
then ask user to choose which to read
then send to LLM to summarise
then do a bit prompt engineering

Loop through your collected results and print each article with a number (1, 2, 3...)
Use input() to ask the user to pick a number
Look up which article that number maps to
"""
from news import get_headlines

tickers_list = ["NVDA", "AAPL"]

ticker_keywords = {
    "NVDA": {"Nvidia", "Semiconductor"},
    "AAPL": {"IPhones"}
}

headline_list = []
for ticker in tickers_list:
    article_list = get_headlines(ticker)
    if article_list:
        headline_list.append(article_list)

for i, news_item in article_list.enumerate():
    print(f"{i}: {news_item.title}")


#call LLM
#SDK is enough, no need langchain langgraph
#SDK = Software development kit
prompt = f"""You are an university professor in Finance, 
        and has rich knowledge in how to dissect finance news and explain it to finance beginners"""

#here we put the chat loop with user
"""while True:
    1. get user input
    2. check if quit → break
    3. append user message to list
    4. call API
    5. print response
    6. append assistant response to list
"""
messages_list = [{"role": "system", "content": "You are a helpful assistant"}]
response_0 = client.chat.completions.create(
  model="deepseek-chat",  # or deepseek-reasoner
  messages=messages_list
)
print(response_0.choices[0].message.content)

while True:
  user_input = input("Enter your message: ")
  if user_input.lower() == "quit":
    break
  messages_list.append({"role": "user", "content": user_input})
  response = client.chat.completions.create(
    model="deepseek-chat",  # or deepseek-reasoner
    messages=messages_list
  )
  print(response.choices[0].message.content)
  messages_list.append({"role": "assistant", "content": response.choices[0].message.content})
