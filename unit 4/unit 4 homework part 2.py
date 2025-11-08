#storing the highs and lows for the next 7 days weather
listofweather= [
    ["saturday", "6, 2"],
    ["sunday", "2, -2"],
    ["monday", "0, -2"],
    ["tuesday", "4, 0"],
    ["wednesday", "7, 4"],
    ["thursday", "7, 2"],
    ["friday", "7, -1"]
]

#asking the user which day they want to know the weather of
weather=input("Which day do you want to know the weather?")

#seeing what to print depending on user's input
if weather=="saturday" or weather=="Saturday":
    print(listofweather[0][1])
elif weather=="sunday" or weather=="Sunday":
    print(listofweather[1][1])
elif weather=="monday" or weather=="Monday":
    print(listofweather[2][1])
elif weather=="tuesday" or weather=="Tuesday":
    print(listofweather[3][1])
elif weather=="wednesday" or weather=="Wednesday":
    print(listofweather[4][1])
elif weather=="thursday" or weather=="Thursday":
    print(listofweather[5][1])
elif weather=="friday" or weather=="Friday":
    print(listofweather[6][1])

else:
    print("please put in a real day")
