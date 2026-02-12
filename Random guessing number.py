import random
cnumber=random.randint(1,100)
userinput=int(input("Enter a number between 1 and 100: "))
print("Computer Number -",cnumber)
if cnumber>userinput:
    print("Your guess is too high")
elif cnumber<userinput:
     print("Your guess is too low")
else:
     print("You guess is Equal")
