import openai
import os
from dotenv import load_dotenv, find_dotenv
_=load_dotenv(find_dotenv())
openai.api_key=os.getenv('OPENAI_API_KEY')

def get_completion(prompt,model='gpt-3.5-turbo'):
	messages=[{"role":"user","content":prompt}]
	response=openai.ChatCompletion.create(
	model=model,
	messages=messages,
	temperature=0,
	)
	return response.choices[0].message["content"]

story=f"""

The Supreme Court ordered the constitution of a five-member special investigation team (SIT) under Central Bureau of Investigation (CBI) director’s \
supervision.The Supreme Court on Friday ordered a fresh investigation into the allegations that the Tirumala Tirupati Devasthanams (TTD) laddu prasadam \
contained ghee adulterated with animal fat, underlining that the issue ought not to be “turned into a political drama” and that the probe was meant\ 
“to assuage the concerns and sentiments of millions of devotees across the globe.”\
A bench of justices Bhushan R Gavai and KV Viswanathan ordered the constitution of a five-member special investigation team (SIT) under the Central \
Bureau of Investigation (CBI) director’s supervision for the probe. The SIT will include two officers each from the CBI, the Andhra Police, and a \
Food Safety and Standards Authority of India (FSSAI) member.\
Participate in the Festival of Gifts & get a chance to win an iPhone 15 and other exciting prizes. Play Now!\
“We clarify that we will not permit the court to be used as a political battleground. ...to assuage [the] feelings of crores of people,\
 we find that investigation by an independent SIT consisting of representatives of state police, CBI, and FSSAI, should be done. We also direct that\
 investigation should be under the supervision of the director of CBI,” said the bench.\
The bench clarified that the order for the fresh investigation does not reflect either on the accusations some of the petitioners have made about the\
 independence of the members of the state government’s probe panel or their fairness.\
“We further clarify that our order should not be construed as a reflection on the independence and fairness of the members of the state SIT. We have\
 constituted the committee only to assuage the feelings of crores of people having faith in the deity [Lord Venkateshwara],” said the court, wrapping\
 up the proceedings.\
The order came after the Union government, represented by solicitor-general Tushar Mehta, agreed to intervene and verify the claims. Mehta said that \
the state’s SIT had competent members and that a central team could assist and oversee the investigation.\
The bench said it would be more appropriate for a central agency like the CBI to get involved. “Let there be an independent SIT with two officers from\
 CBI, two from state government and one from FSSAI. It can also be supervised by the CBI director. You do it so that there is more confidence in the \
process,” said the bench. “We do not want this to turn into a political drama. There are sentiments of crores of devotees from across the world involved.”\
The order came after the bench expressed concerns over conflicting reports and public statements made during the earlier investigation. In its hearing on\
 September 30, the court chastised Andhra Pradesh chief minister N Chandrababu Naidu for prematurely going public with allegations before the investigation\
 was completed.\
“There is absolutely no evidence yet to substantiate the claim that ghee adulterated with animal fat was used in the laddus,” the bench said on September \
30. The court also halted the state government’s probe and warned of the dangers of public figures making premature statements in such a sensitive matter.\
The controversy was sparked on September 18 when Naidu accused his predecessor, YS Jagan Mohan Reddy, of permitting the use of substandard ingredients, \
including animal fat, in making the laddu prasadam. Naidu cited a lab report from the National Dairy Development Board, which he claimed confirmed the\
 presence of beef tallow, fish oil, and lard in the ghee supplied for making the prasadam.\
This claim triggered protests across Andhra Pradesh. Naidu’s rivals in the YSR Congress Party (YSRCP) accused him of playing politics with religious \
sentiments. YSR Congress leader Vellampalli Srinivas criticised Naidu for making “baseless and irresponsible” allegations, further fuelling the political \
controversy.\
On Friday, Mehta assured the court that the Union government would step in, involving experts from the FSSAI, to examine ghee and laddu samples.\
 “One thing is very clear if there is any truth in the claims [of adulteration], it is unacceptable,” Mehta said.\
The bench agreed. “Nobody can doubt that if there is any truth in the claims, it is very serious.”\
Senior counsel Mukul Rohatgi and Sidharth Luthra, appearing for the state government and TTD, agreed with Mehta’s suggestion. They said they have no\
 problem with a central team stepping in. The two lawyers submitted that some of the media reports presented before the court were not true reproductions\
 of either the turn of events or the timeline of statements.\
Luthra questioned the bonafide of YSRCP lawmaker and former TTD Board chairman YV Subba Reddy’s plea. He pointed out the plea was an exact copy of \
Bharatiya Janata Party leader Subramanian Swamy’s petition. Luthra said it contained the same spelling errors made in Swamy’s petition. “He [Reddy] \
has also concealed material facts from this court about the pendency of a similar plea in the high court. This man is under investigation in the same \
matter,” Luthra said.\
Senior counsel Kapil Sibal, appearing for Reddy, said that Naidu’s statements on the issue cast serious doubts on the independence of the state’s probe \
and that the court should order a fresh probe.\
Mehta intervened saying the matter involves faith. He urged the bench to ensure it is not given a political colour. The bench agreed with him and asked \
Mehta to involve CBI in the probe and ordered a new SIT.\
The sacred laddu prasadam is an essential offering for the nearly 90,000 daily visitors to the Tirumala Temple, considered one of Hinduism’s most \
significant shrines. The temple sells nearly 10 million laddus monthly, generating over ₹500 crore in revenue annually.\
Petitioners, including spiritual speaker Dushyanth Sridhar and historian Vikram Sampath, called for a court-supervised committee to investigate \
the allegations. They argued that the preparation of laddus is a religious practice protected under the Constitution’s Article 25, which guarantees \
freedom of religion, and that any adulteration would be a violation of that sacred tradition.\
"""

prompt=f"""
Detrmine 5 topics that are being discussed in the story delimitted by triple backtics.\
Format and display your response in a list seperated by commas where each item \
can be one or two words long \
story=```{story}```

"""
response=get_completion(prompt)
print(response)

topic_list=['Laddu prasadam','Political drama','Adulteration']
response.split(sep='\n')


prompt=f"""
Determine whether each item in the list of topics is present in the story below\
delimitted by triple backtics. Give your response as follows:\
Item from the list:0 or 1
List of Topics : {",".join(topic_list)}
story: ```{story}```
"""

response=get_completion(prompt)
#print(response)

news_list=response.split("\n")
#print (news_list)

news_dict={

    i.split(':')[0]:int(i.split(':')[1])
    for i in news_list
    }
#print(news_dict)

if news_dict['Laddu prasadam']==1:
    print("New Laddu Prasadm Story")
