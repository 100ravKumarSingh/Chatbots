import openai
import os
from dotenv import load_dotenv,find_dotenv
_=load_dotenv(find_dotenv())
openai.api_key=os.getenv('OPENAI_API_KEY')



def get_completion(prompt,model='gpt-3.5-turbo'):
	messages=[{"role":"user","content":prompt}]
	response=openai.ChatCompletion.create(
		messages=messages,
		model=model,
		temperature=0,
		)
	return response.choices[0].message["content"]

text1=f"""

Rivers were flodded with Water.

Why were the Rivers flodded with water?
-Because it was raining heavily.

Why it was raining heavily?

-Because it is the rainy season and it is expected to rain.


why..."""

prompt1=f"""generate a series till 5 whys in  the  reference of {text1}\
and print from 1st why"""

response=get_completion(prompt1)
print(response)