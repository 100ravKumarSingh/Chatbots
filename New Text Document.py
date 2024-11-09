import openai
import os
from dotenv import load_dotenv,find_dotenv
_=load_dotenv(find_dotenv())
openai.api_key=os.getenv('OPENAI_API_KEY')

#get_completion----
def get_completion(prompt,model='gpt-3.5-turbo'):
    messages=[{"role":"user","content": prompt}]
    response=openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0,
    )
    return response.choices[0].message["content"]

#get_completion_from_messgaes
def get_completion_from_messages(messages,model='gpt-3.5-turbo'):
    response=openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0,
    )
    return response.choices[0].message["content"]
    

#system instruction-------
instruction=f"""You are a customer support AI assistant, an automated service to collect opinion of customer.\
You first greet the customer, ask for opinion and analyse the customer's review and determine the sentiment of the review. \
Generate a reply based on the sentiment.\ If the sentiment is positive,\thank the customer. If it is negetive, apologise for\
the inconvinience and suggest that they can reach out to customer care.\Make sure to use specefic details from the review. \
Write in a concise and professional tone."""

context=[{'role':'system','content':f'{instruction}'}]
    

#collect_messages
def collect_messages(_):
    prompt=inp.value_input
    inp.value=''
    context.append({'role':'user','content':f"{prompt}"})
    response=get_completion_from_messages(context)
    panels.append(
        pn.Row('user:', pn.pane.Markdown(prompt, width=300))
    )
    panels.append(
        pn.Row('assistant:', pn.pane.Markdown(response, width=300))
    )
    return pn.Column(*panels)

# display panel 
import panel as pn
pn.extension()
panels=[]
context=[]
inp=pn.widgets.TextInput(value="Hi",placeholder="Enter your text here",height=100)
button=pn.widgets.Button(name="Chat")
interaction=pn.bind(collect_messages, button)
# dashboard
dashboard=pn.Column(
	inp,
	pn.Row(button),
	pn.panel(interaction,loading_indicator=True,height=300)
)
dashboard
