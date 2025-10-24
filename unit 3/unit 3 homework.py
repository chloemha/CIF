#importing randint function
from random import randint 

#asking user to set the range
first=int(input("Enter the first number for the range:"))
second=int(input("Enter the second number for the range: *make sure this number is greater than your first number*"))

#the number created by the user's range
number=randint(first,second)

#setting response to yes for now
again="yes"

#while loop to start the game
while again=="yes" or again=="Yes":
    guess=int(input("Guess a number between your range:"))

    if guess==number:
        print("You won!")
        again="no"
    else:
        print("You lose")

        if guess>number:
            print("Your number is too big")
        if guess<number:
            print("Your number is too small")
        if number%2==0:
            print("The number is even")
        else: 
            print("The number is odd")
        again=input("Do you want to guess again?")
print("bye")