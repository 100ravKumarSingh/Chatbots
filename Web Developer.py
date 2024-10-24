import openai
import os
from dotenv import load_dotenv, find_dotenv
_=load_dotenv(find_dotenv())

def get_completion(prompt,model="gpt-3.5-turbo"):
	messages=[{"role":"user","content":prompt}]
	response=openai.ChatCompletion.create(
	model=model,
	messages=messages,
	temperature=0,
	)
	return response.choices[0].message["content"]

text=f""" Display a slide show with first slide as 'Welcome' \
and second slide as ' We are leading Tutors in English'."""

prompt=f"""get the HTML code to include the {text} at the top of the web page.\
Height  should be 500 pixels. Content should fill the slideand Time interval\
between slides should be 1 sec
"""

response=get_completion(prompt)
print(response)  

from IPython.display import display, HTML
display(HTML(response))