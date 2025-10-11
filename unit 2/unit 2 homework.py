from random import randint

number=randint(1,20)

answer=int(input("Enter a number from 1 to 20"))

if answer==number:
    print("You win!")
else:
    print("You lose, try again")