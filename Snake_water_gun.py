import random
'''
1 for Snake
-1 for water
0 for gun
'''

computer = random.choice([1, -1, 0])

youstr = input("Enter your choice: ")
youdict = {"s": 1, "w":-1, "g":0 }
reversedict = {1:"Snake",-1:"Water",0:"Gun"}
you = youdict[youstr]

print(f"Computer chose {reversedict[computer]}\nYou chose {reversedict[you]}")

if computer == you:
    print("it's a Draw")

else:   
    if computer == -1 and you == 1:
        print("You Win!")
    elif computer == -1 and you == 0:
        print("You Lose!")
    elif computer == 1 and you == -1:
        print("You Lose!")
    elif computer == 1 and you == 0:
        print("You Win!")
    elif computer == 0 and you == 1:
        print("You Lose!")
    elif computer == 0 and you == -1:
        print("You Win!")
    else:
        print("Something is not right??")
