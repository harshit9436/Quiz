import requests
import pprint
import json
import random

score=0
c="hy"
print()
print("heyy!! let's take a quiz. The questions are either multiple choice answer or True-false type.")
while c!="quit":
    number=1
    r = requests.get("https://opentdb.com/api.php?amount=1&difficulty=easy")
    b = json.loads(r.text)
    answer=[]
    correct_answer=b["results"][0]["correct_answer"]
    answer.append(correct_answer)
    incorrect_answer=b["results"][0]["incorrect_answers"]
    if len(incorrect_answer)==3:
        answer.append(incorrect_answer[0])
        answer.append(incorrect_answer[1])
        answer.append(incorrect_answer[2])
    else:
        answer.append(incorrect_answer[0])
    random.shuffle(answer)
    print()
    print('The category of your question is:', b["results"][0]["category"])
    print()
    print("question :",b["results"][0]["question"])
    for i in answer:
        print(number ,end="")
        print(" - ",end="")
        print(i)
        print()
        number+=1

    y= int(input("enter the answer number."))
    print()
    print(answer.index(b["results"][0]["correct_answer"])+1)
    if y==(answer.index(b["results"][0]["correct_answer"])+1):
        print("your answer is correct")
        print()
        score+=1
    else:
        print("your answer is incorrect.")
        print("correct answer is ", b["results"][0]["correct_answer"])
        score+=0
    c=input("if you wanna quit, type quit , to continue press enter ")
    print("-----------------------------------------------------")
    if c=="quit":
        break
    else:
        continue
print("Thanx for taking the quiz")
print("your score is:", score)