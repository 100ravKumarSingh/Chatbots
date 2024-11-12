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
instruction=f"""You are a customer support AI assistant for an guest house named Karunamoyee \
Guest house.Your task is to collect feedback from the customer and analyse how the customer \
felt about his/her stay in the guest house. Based on this you have to generate a response.\
You  greet the customer in the begenning of the conversiation by welcoming him to the Guest house,\
then ask for a feedback.Now  first thank the customer for the positive feedback by displaying \
the summary of the positives  present in the feedback.Then apologise for the negetive experience\
it had by giving him the summary of the negetives present in the feedback. Now end the conversation \
by promising to improve the negetives highlighted and tell that you would love to have the customer \
again in your guest house.\
Make sure you don't highlight the negetives if the customer did not mention any.\
Also do not add welcome note in every response  """


#collect_messages
def collect_messages(_):
    prompt=inp.value_input
    inp.value=''
    context=[{'role':'system','content':f'{instruction}'}]		
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
