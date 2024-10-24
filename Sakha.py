import openai
import os
from dotenv import load_dotenv, find_dotenv
_=load_dotenv(find_dotenv())
openai.api_key=os.getenv('OPENAI_API_KEY')

def get_completion(prompt):
	msg=[{"role":"user","content":prompt}]
	response=openai.ChatCompletion.create(
	model='gpt-3.5-turbo',
	temperature=0,
	messages=msg,
	)
	return response.choices[0].message["content"]

txt=f"""\
I am a 27 year old living in Jamshedpur.\
Jamshedpur is my  Birthplace and I love it.\
I live here with my family.Recently I joined a private firm as an Engineer.\
I am somewhat satisfied working here as the compensation given is good and co-workers \
are also cooperative. But recent RTO push has craeted restleness in my life.\
Having family health issues to look after , it's very difficult for me to rellocate.\

Now making a choice to switch to some other local company for a less package or to rellocate\
against  an expense of accomodation is making life difficult. Hope I come out\
of this situation ASAP.
"""

prompt=f""" tell me  about myself  giving all details provided by me in the text \
delimitted by triple backtics \explaining simultaneously  my  emotions wherever present\
in text. After this list down all emotions I am feeling while writing this text giving\
a reason beside the list items why you feel this emotion is present.\ And then tell me \
which emotions are negetive and how to overcome them.
text=```{txt}```"""

response=get_completion(prompt)
print(response)