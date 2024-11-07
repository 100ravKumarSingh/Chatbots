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
Your task is to analyse the customer review and generate a reply based on the sentiment.\
Analyse the review delimited by  ``` and create a response. If the sentiment given in <> is positive,\
thank the customer. If it is negetive, apologise for the inconvinience and suggest that they can reach out to customer care.\
Make sure to use specefic details from the review. Write in a concise and professional tone.\
Review:```{review}``` \
sentiment: <{sentiment}>"""

response=get_completion(prompt)
print(response) 
#get_completion_from_messgaes
def get_completion_from_messages():
    

#collect_messages
def collect_messages(_):
    prompt=inp.value_input
	inp.value=''
    context.append({'role':'user','content':f"{prompt}"})
    response=get_completion_from_messages(context)
    panels.append(
        pn.Row('user:', pn.pane.Markdown(prompt, width="300"))
    )
    panels.append(
        pn.Row('assistant:', pn.pane.Markdown(response, width="300"))
    )
    return pn.column(*panels)

# display panel 
import panel as pn
pn.extension()
panels=[]
context=[]
inp=pn.widgets.TextInput(value="Hi",placeholder="Enter your text here")
button=pn.widgets.Button(name="Chat")
interaction=pn.bind(collect_messages, button)
# dashboard
dashboard=pn.column(
	inp,
	pn.Row(button),
	pn.panel(interaction,loading_indicator="true",height=300)
)
dashboard
	
   
    
