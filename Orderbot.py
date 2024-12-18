import openai
import os
from dotenv import load_dotenv, find_dotenv
_=load_dotenv(find_dotenv())
openai.api_kry=os.getenv("OPENAI_API_KEY")

    
def get_completion_from_messages(messages,model='gpt-3.5-turbo',temperature=0):
    response=openai.ChatCompletion.create(
    messages=messages,
    model=model,
    temperature=temperature,
    )
    return response.choices[0].message["content"]


def collect_messages(_):
    prompt=inp.value_input
    inp.value=''
    context.append({'role':'user','content':f"{prompt}"})
    response=get_completion_from_messages(context)
    context.append({'role':'assistant','content':f"{response}"})
    
    panels.append(
    pn.Row('user: ', pn.pane.Markdown(prompt, width=300))
    )
    panels.append(
    pn.Row('assistant: ',pn.pane.Markdown(response, width=300,  style={'background-color':'yellow'}))
    )
    return pn.Column(*panels)

import panel as pn
pn.extension()
panels=[]
context=[{'role':'system','content':"""
You are OrderBot, an automated service to collect orders for a pizza restaurant. \
You first greet the customer, then collects the order, \
and then asks if it's a pickup or delivery. \
You wait to collect the entire order, then summarize it and check for a final \
time if the customer wants to add anything else. \
If it's a delivery, you ask for an address. \
Finally you collect the payment.\
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
You respond in a short, very conversational friendly style. \
The menu includes \
pepperoni pizza  12.95, 10.00, 7.00 \
cheese pizza   10.95, 9.25, 6.50 \
eggplant pizza   11.95, 9.75, 6.75 \
fries 4.50, 3.50 \
greek salad 7.25 \
Toppings: \
extra cheese 2.00, \
mushrooms 1.50 \
sausage 3.00 \
canadian bacon 3.50 \
AI sauce 1.50 \
peppers 1.00 \
Drinks: \
coke 3.00, 2.00, 1.00 \
sprite 3.00, 2.00, 1.00 \
bottled water 5.00 \
"""
}]
inp=pn.widgets.TextInput(value="Hi",placeholder="Enter your text here")
button=pn.widgets.Button(name='chat')
interact=pn.bind(collect_messages, button)
dashboard=pn.Column(
inp,
pn.Row(button),
pn.panel(interact,loading_indicator=True, height=300),

)
dashboard
