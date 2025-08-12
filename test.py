import random
#Snake Water Gun game
'''
snake = 1
water = -1
gun = 0
'''

computer = random.choice([1,-1,0])
print("You are playing Snake water gun game good luck")

youstr = input("Enter your choice s,w,g : ") #only enter s,w,or g
youdict = {"s":1,"w":-1,"g":0}

reversedict = {1:"snake",-1:"water",0:"gun"}

you = youdict[youstr.lower()]

print(f"Computer chose {reversedict[computer]}\nYou chose {reversedict[you]}")


if computer==you:
    print("Its a Draw!, How can you read each others mind holysheettts!!!")
elif computer == 1 and you == -1:
    print("You lose \nThe Snake quenched his thirst!")
elif computer == 1 and you == 0:
    print("You won \nSnap!! you shot the snake right in the head yo")
elif computer == -1 and you == 1:
    print("You Won \nQuenched your thirst?")
elif computer == -1 and you == 0:
    print("You lose \nnever bring a gun in a water fight again!")
elif computer == 0 and you == 1:
    print("You lose \nSnap!! your Snake got shot right in the head yo!")
elif computer == 0 and you == -1:
    print("You won \nDrown that stupid gun!")
else:
    print("Something ain't right")
