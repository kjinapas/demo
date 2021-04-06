# import random
# passlen=int(input())
# s="abcdefghijklmnopqrstuvwxyz!@#$%^&*()?"
# i=0
# randomdata=[]
# while i<passlen:
#     p = "".join(random.sample(s, 20))
#     randomdata.append(p)
#     i+=1
#
#
#
# print('\n'.join([f"Your Password Number {i+1} is : "+str(randomdata[i]) for i in range(len(randomdata))]))
import time
import random
name= input("What is your name")
time.sleep(1)
words=['Hello','hfjifgjfi']
word = random.choice(words)
guesses=" "
turn =5
while turn > 0:
    failse =0
    for char in word:
        if char in guesses:
            print(char,end="")
        else:
            print("_",end="")
            failse+=1
    if failse==0:
        print("\nYou Won")
        break
    guess=input("\nquess a character:")
    guesses+=guess
    if guess not in word:
        turn-=1
        print("\nYou Wrong")
        print("\nyou have",+turn,'more guesses')
        if turn ==0:
            print('\nyour lose')