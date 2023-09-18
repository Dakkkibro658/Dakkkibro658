print("My Name Is Dakkibro658 and I am Creator of This Game")
user_name = input("Enter Your Name:")
print("Hello",user_name,"let's Play Snake, Water and Gun")
import random
print("-"*100)
print("Snake(1),Water(2),Gun(3) Or Choose (4) to quit")
n = 1
while n > 0:
    you = eval(input("Enter Your Choice:"))
    if you == 4 or 0:
        print("You Quit The Game!")
    elif you > 4:
        print("Sorry , Wrong Input!")
    else:
        comp = random.randint(1, 3)
        print("Computer choose : ",comp)
        if you == comp:
            print("That's a Tie")
        elif you == 1 and comp == 2:
            print("You Win!")
        elif you == 1 and comp == 3:
            print("You Lose!")
        elif you == 2 and comp == 3:
            print("You Lose!")
        elif you == 2 and comp == 1:
            print("You Lose!")
        elif you == 3 and comp == 2:
            print("You Win!")
        elif you == 3 and comp == 1:
            print("You Win!")
        else:
            pass
