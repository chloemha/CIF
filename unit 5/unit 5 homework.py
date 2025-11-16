#import random function
from random import randint

#introduction
def beginning():
    instructions= ["\nWelcome to the Harry Potter game!", "Instructions:", "1. You have recieved your Hogwarts letter, and you have taken the train to Hogwarts", "2. Go to the sorting ceremony to get sorted into your house", "3. Take the following class:", "- charms/defense against the dark arts", "4. Answer questions corectly to earn points!"]
    for i in instructions:
        print(i)

beginning()

#setting the points up
points=0

#the sorting ceremony
def sorting_ceremony():
    print("\nWelcome to the Sorting Ceremony! Please have a seat, and the sorting hat will be placed on your head.")
    personality= input("Are you smart, kind, brave, or ambitious?")
    if personality=="smart" or personality=="Smart":
        house = "Ravenclaw"
    elif personality=="kind" or personality=="Kind":
        house = "Hufflepuff"
    elif personality=="brave" or personality=="Brave":
        house = "Gryffindor"
    elif personality=="ambitious" or personality=="Ambitious":
        house = "Slytherin"
    print(f"You are a {house}")

sorting_ceremony()

#transition into class
print("\nNow it's time for charms/defense against the dark arts class!")

#the charms/defense against the dark arts class
def charms():
    print("Welcome to Charms Class with Mr. Flitwick and Mr. Lupin! You will be learning different spells, and you will be tested after learning them. Pay attention!\n")
    information=["Spells:", "Expelliarmus - used to disarm an opponent", "Wingardium Leviosa - used to make an object fly", "Alohomora - used to unlock doors", "Unforgiveable curses - banned by the ministry, never to use"]
    for a in information:
        print(a)
    print("\nNow it's time for your test. Answer the following questions:")
    charms_questions=[
        ["What spell is used to make an object fly?", ["wingardium leviosa", "Wingardium Leviosa", "Wingardium leviosa"]],
        ["What is the general name for the spells that are banned by the ministry?", ["unforgiveable curses", "Unforgiveable Curses", "Unforgiveable curses"]],
        ["What spell is used to disarm an opponent?", ["expelliarmus", "Expelliarmus"]],
        ["What spell is used to unlock doors?", ["alohomora", "Alohomora"]]
    ]
    
    #if it is false, it means the question has already been done before
    questions_done=[False, False, False, False]
    
    #checking to see if the answer is right, and then adding points
    def checkanswer(questiontext):
        global points
        answer = input(questiontext)
        if (answer in charms_questions[question_number][1]):
            points+=1
            print("Correct")
        else:
            print("Wrong")
    
    #when the question isn't done yet
    while False in questions_done:
        question_number=randint(0, 3)
        while (questions_done[question_number]):
            question_number=randint(0, 3)

        questions_done[question_number]=True #when the question has been done
        question=charms_questions[question_number][0]
        checkanswer(question)

charms()

#short conclusion
print("You have completed your first day at Hogwarts and earned", points, "points! Have a great rest of your night!")