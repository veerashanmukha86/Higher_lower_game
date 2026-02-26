import art as art
import random as r
import pandas as pd
import pandas as pd
data=pd.read_csv("insta_50_data.csv")
data=data.to_dict("records")
# print(data)
print(art.logo)
score = 0
a = r.randint(0, 49)
b = r.randint(0, 49)
num1 = a
num2 = b
def printscore(score,ans1,ans2):
    print("\n" * 100)
    print("Your guess correct your score incresed")
    print(f"Your score is {score}")
    if ans1<ans2:
         print(f"Rank of A is {ans1} and Rank of B is {ans2}")
    else:
        print(f"Rank of B is {ans2} and Rank of A is {ans1}")

def printover():
    print(f"Your guess is wrong ")
    print(f"Your score: {score}")
    print("Game over")
def prints(num1,num2):
    print(f"Compare A {data[num1]["Owner"]},a {data[num1]["Profession_or_Activity"]}, from {data[num1]["Country"]}")
    print(art.vs)
    print(f"Compare B {data[num2]["Owner"]},a {data[num2]["Profession_or_Activity"]}, from {data[num2]["Country"]}")
while True:
    prints(num1,num2)
    ans1=data[num1]["Followers(millions)"]
    ans2=data[num2]["Followers(millions)"]
    option=input("Who has more followers? Type A/a or B/b: ")
    if option=="A" or option=="a":
        if ans1>ans2:
            score+=1
            printscore(score,data[num1]["Rank"],data[num2]["Rank"])
            num1=num1
        else:
            printover()
            break
        num2=r.randint(1, 50)
    if option=="B" or option=="b":
        if ans1<ans2:
            score+=1
            printscore(score,data[num1]["Rank"],data[num2]["Rank"])
            num1=num2
            
        else:
            printover()
            break
        num2=r.randint(1, 50)




