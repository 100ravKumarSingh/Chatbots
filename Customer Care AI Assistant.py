import openai
import os
from dotenv import load_dotenv,find_dotenv
_=load_dotenv(find_dotenv())
openai.api_key=os.getenv('OPENAI_API_KEY')

def get_completion(prompt,model='gpt-3.5-turbo'):
    messages=[{"role":"user","content": prompt}]
    response=openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0,
    )
    return response.choices[0].message["content"]
    
review=f"""Best place to plan your stay.\
Good facilities available at affordable prices. The attached washroom in every room  is an\
advantage.\
The location is  quiet , reachable and   close to the market.\
The manager is  polite .\
Highly recommended."""

prompt=f"""what is the sentiment of the review delimited by triple backticks.\
Review : ```{review}```
"""  
sentiment=get_completion(prompt)

prompt=f"""You are a customer support AI assistant.\
Your task is to analyse the customer review and generate a replay based on the sentiment.\
Analyse the review delimited by  ``` and create a response. If the sentiment given in <> is positive,\
thank the customer. If it is negetive, apologise for the inconvinience and suggest that they can reach out to customer care.\
Make sure to use specefic details from the review. Write in a concise and professional tone.\
Review:```{review}``` \
sentiment: <{sentiment}>"""

response=get_completion(prompt)
print(response)  