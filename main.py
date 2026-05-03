"""
main.py
CLI chatbot entry point
"""
from news import get_headlines
from chat import chat

def greet():
  user_name = input("User name: ")
  print(f"""
  --------------- News Chatbot ---------------
  Good morning, {user_name}!
  Another day, another headline!
  Which of the following topics are you interested?
  1. Economics 
  2. Sports
  3. Technology
  """)
  topics = [(1, "Economics"), (2, "Sports"), (3, "Technology")]
  
  count = 0
  while count < 3:
    topic = input("Topic: (1/2/3)")
    try:
      topic = int(topic)
      break
    except:
      print(f"Incorrect input, please try again. You have {count} more chances")
      count += 1

  return user_name, topics[topic-1][1]


def display_headlines(articles):
  headlines = [(i, article.get("title", "")) for i, article in enumerate(articles)]
  for headline in headlines:
    print(f"{headline[0]+1}: {headline[1]}")

def chat_loop(user_name, messages):
  while True:
    user_input = input(f"{user_name}: ")
    if user_input.lower() == "quit":
      break
    messages.append({"role": "user", "content": user_input})
    reply = chat(messages)
    print(f"bot: {reply}")
    messages.append({"role": "assistant", "content": reply})



#call LLM
system_prompt = f"""You are an execellent news summarization assistent. Please summarize the given article according to the following format:
title
area
date
point form summary
extract key insights from the article
"""



def main():
  user_name, topic = greet()
  articles = get_headlines(topic)
  display_headlines(articles)
  chosen = int(input("choose headline to summarise: "))
  
  messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": f"Here are the articles I want to discuss: {articles[chosen-1]}"}
  ]
  print(chat(messages))
  chat_loop(user_name, messages)


if __name__ == "__main__":
  main()