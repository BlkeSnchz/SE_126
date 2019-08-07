#Blake Sanchez, SE_126, 7/17/2019, Lab 1 C
print("Welcome to Blake's Fire Safety Determinator.")
capacity = 0 #room
attendees = 0 #people
register = 0 #amount
ans = "y"

while (ans == "y") or (ans == "Y"):
    capacity = int(input("Please enter the Maximum Room Capacity: "))
    attendees = int(input("Please enter the amount of attendees participating in the meeting: "))
    register = capacity - attendees
    if (attendees <= capacity):
        print("Good News! The meeting is Legal and {0} additonal attendees may attend.".format(register))
    elif (attendees > capacity):
        print("Bad News! The meeting cannot be held as planned due to the fire regulation. {0} attendees must be excluded in order to meet the fire regulations.".format(register))
    else:
        print("The number's you have entered resulted in an error. Please try again.")
    ans = input("Would you like to try a different combination?: [y/n]")
print("Thank you for using Blake's Fire Safety Determinator. Stay Safe.")