import openai
import os
from dotenv import load_dotenv , find_dotenv
_=load_dotenv(find_dotenv())
openai.api_key=os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model='gpt-3.5-turbo'):
    messages=[{"role": "user" ,"content":prompt}]
    response=openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0,
    )
    return response.choices[0].message['content']
    

user_messages=[
"আমি আমার ল্যাপটপ চালু করতে পারছি না",
"मी माझा लॅपटॉप चालू करू शकत नाही",
"ું મારા લેપટોપ પર સ્વિચ કરી શકતો નથી"
]
for issue in user_messages:
    prompt=f"Tell me what language this is  ```{issue}```"  
    lang=get_completion(prompt)
    print(f"Original message ({lang}):{issue}")
    prompt=f"""Translate the text  into english and Hindi\
    ```{issue}```"""
    response=get_completion(prompt)
    print(response,"\n")
    

