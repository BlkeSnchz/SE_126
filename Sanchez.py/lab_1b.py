#Blake Sanchez, SE126, 7/16/2019, Lab 1 B
print("Welcome to Blake's Fire Safety Determinator.")
room = 0
people = 0
ans = "y"

#def main():
     #while (ans != "y" or ans != "Y" or ans != "n" or ans != "N"):
        #check = input("Do you want to check anymore rooms? [y/n]")
        
        #if (ans == "y" or ans == "Y"):
           
        #elif (ans == "n" or ans == "N"):
        #    print ("Thank you.")
        #else:
         #   print("You should enter either Y/y or N/n.")
        #return

while (ans == "y" or ans == "Y"):
    room = int(input("Please enter the Maximum Room Capacity: "))
    people = int(input("Please enter the amount of people attending the meeting: "))
    amount = room - people
    if (people <= room):
        
        print("Good News! The meeting is Legal and {0} additonal people may attend.".format(amount))

    elif (people > room):
        print("Bad News! The meeting cannot be held as planned due to the fire regulation. {0} people must be excluded in order to meet the fire regulations.".format(amount))
    else:
        print("The letter you have entered resulted in an error. Please try again.")
    ans = input("Do you want to check again?: [y/n]")
    while (ans != "y" and ans != "Y" and ans != "n" and ans != "N"):
        print("Error please enter a valid answer: [Y/y for 'Yes' or N/n for 'No']")
        ans = input("Do you want to check again?: [y/n]")
print("Thank you for using Blake's Fire Safety Determinator!")       
    
#while ans == "Y" or ans == "y":
        #room = int(input("Please enter the Maximum Room Capacity: "))
        #people = int(input("Please enter the amount of people attending the meeting: "))
        #amount = room - people
        #if ans == "n" or ans == "N":
            #print("Thank you for using Blake's Program.")
            
    #while (ans == "y" or ans == "Y"):
       # if (ans == "N" or ans == "n"):
        #    print("Thank you for using Blake's Fire Safety Determinator!")
        #else:
    #ans = input("Do you want to check again?: [y/n]")





#------------------------------
#room = int(input("Please enter the Maximum Room Capacity: "))
#        people = int(input("Please enter the amount of people attending the meeting: "))
 #       amount = room - people
  #  if(ans == "n" or ans == "N"):
   #      print("Thank you.")
    #else:
     #   ans = input("Do you want to check again?: [y/n]")
