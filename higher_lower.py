from logo import logo, vs
from data_base import data
import random
import os
def choose_question2(question1):
    question2=random.choice(data)
    while (question1==question2):    
        if question1==question2:
            question2=random.choice(data)
    return question2
def formatData(question):
    '''Let's format the data here'''
    name=question['name']
    follower_count=question['follower_count']
    description=question['description']
    country=question['country']
    return f"   '{name}',  '{description}',  {country}"
def result(ans, question1, question2):
    Ans='a'
    if(question1['follower_count']>question2['follower_count']):
        Ans='a'
    else:
        Ans='b'
    if(ans==Ans):
        return True
    else:
        return False
print(logo)
question1=random.choice(data)
run=True
score=0
while(run):
    question2 = choose_question2(question1)
    print(f"Compare A:{formatData(question1)}.")
    print(vs)
    print(f"Compare B:{formatData(question2)}.")
    ans=input('Who has more Instagram followers : choose from  A or B : ').lower()
    if(result(ans, question1,question2)):
        os.system('cls')
        question1=question2
        score +=1
        print(f"YOUR CURRENT SCORE: {score}")
        print(logo)
    else:
        run=False
        print(f"\nYOUR CURRENT SCORE: {score}")
        print("SORRY! PLEASE TRY AGIAN.\n")