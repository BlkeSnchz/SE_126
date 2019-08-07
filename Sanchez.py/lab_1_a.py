#Blake Sanchez, SE126, 7/16/2019, Lab 1 A
print("Welcome to Blake's Fire Safety Determinator.") #Welcome the user
room = 0 #variable for room capacity
people = 0 #variable for amount of people
amount = 0 #variable for the total amount 
ans = "y" #answer will equal "Yes" a.k.a. "Y"

#Enter While Loop
while (ans == "y") or (ans == "Y"):
    #Ask the user what the Max. Capacity the Room can hold.
    room = int(input("Please enter the Maximum Room Capacity: "))
    #Ask the user how many people are attending the meeting.
    people = int(input("Please enter the amount of people attending the meeting: "))
    #Use the following equation to determine if the meeting is legal or illegal.
    amount = room - people
    #The following shows that if there are less people than the Max Capacity of the room then the User is all good!
    if (people <= room):
        print("Good News! The meeting is Legal and {0} additonal people may attend.".format(amount))
    #The following shows that if the amount of people is greater than the alotted room Max. Capacity, then the meeting is illegal and some attendees may not be allowed to enter.
    elif (people > room):
        print("Bad News! The meeting cannot be held as planned due to the fire regulation. {0} people must be excluded in order to meet the fire regulations.".format(amount))
    #The else statement will tell the user if what they have entered is invalid.
    else:
        print("The number's you have entered resulted in an error. Please try again.")
    #ans means that we have the ability to loop back into the While if the User responds with "Y" or "y". If the User chooses "N" or "n" then the program will exit the loop.
    ans = input("Would you like to try a different combination?: [y/n]")
#Thank the user for using the program.
print("Thank you for using Blake's Fire Safety Determinator. Stay Safe.")