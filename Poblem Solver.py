import openai
import os
from dotenv import load_dotenv,find_dotenv
_=load_dotenv(find_dotenv())
openai.api_key=os.getenv("OPENAI_API_KEY")

def get_completion(prompt,model='gpt-3.5-turbo'):
	messages=[{"role":"user","content":prompt}]
	response=openai.ChatCompletion.create(
		model=model,
		messages=messages,
		temperature=0,
	)
	return response.choices[0].message["content"]


text=f"""
Question-Ram bought 2 apples.For Rs. 20. He sold them for Rs.30.\
How much profit did Ram earn on reach apple?

student's answer-
Total apples bought=2.
Cost of total apples=20.
Cost of each apple=9.
Total cost of apples sold=30.
Each apple sold for =15.
So profit on each apple= 15-9=6.

So 6 is the answer.

"""	

prompt=f"""Do the  following:-\
1. Display the question from {text} .\
2. Display student's final answer \
3.Now calculate your own solution to find the correct answer.\
4. Determine if Student's answer is also correct  or not?.\
5. If it is  only then display that answer is correct.\
6.If student made a mistake then point out where he did.


"""

response=get_completion(prompt)
print(response)
