import random
import sys

#Initialize Variables
Name=""
question=""
r_digit1=0
r_digit2=0
r_digit3=0
r_digit4=0
g_digit1=0
g_digit2=0
g_digit3=0
g_digit4=0
count=1

#Creating Main Menu
Name=input("Enter Player Name:")
print("Hi",Name,"Welcome to GameInt")
print("Colour Mapping - White=1,Blue=2,Red=3,Yellow=4,Green=5,Purple=6")
print("You Are Ready To Play The Game")

#Inputing Random Numbers
r_digit1=random.randint(1,6)
r_digit2=random.randint(1,6)
r_digit3=random.randint(1,6)
r_digit4=random.randint(1,6)

#Getting User Inputs
while(count<=8):
    if(count==1):
        print("Attempt Number 1")
    elif(count==2):
        print("Attempt Number 2")
    elif(count==3):
        print("Attempt Number 3")
    elif(count==4):
        print("Attempt Number 4")
    elif(count==5):
        print("Attempt Number 5")
    elif(count==6):
        print("Attempt Number 6")
    elif(count==7):
        print("Attempt Number 7")
    else:
        print("Attempt Number 8")
    print(" *Enter a Digit Between 1 and 6\n *Enter 0000 digits to terminate the game")
    g_digit1=int(input("Enter Your Guessing Digit 1:"))
    if(g_digit1>6 or g_digit1<1):
        print("ERROR:\n *Entered Digit Is Not In Range.Please Enter a Digit Between 1 and 6")
    g_digit2=int(input("Enter Your Guessing Digit 2:"))
    if(g_digit2>6 or g_digit2<1):
        print("ERROR:\n *Entered Digit Is Not In Range.Please Enter a Digit Between 1 and 6")
    g_digit3=int(input("Enter Your Guessing Digit 3:"))
    if(g_digit3>6 or g_digit3<1):
        print("ERROR:\n *Entered Digit Is Not In Range.Please Enter a Digit Between 1 and 6")
    g_digit4=int(input("Enter Your Guessing Digit 4:"))
    if(g_digit4>6 or g_digit4<1):
        print("ERROR:\n *Entered Digit Is Not In Range.Please Enter a Digit Between 1 and 6")
    if(g_digit1==0 and g_digit2==0 and g_digit3==0 and g_digit4==0):
        print("The Game Is Terminated")
        quit()
        
#Comparing Random Numbers and User Inputs
    if(r_digit1==g_digit1):
        print("1")
    elif(r_digit1==g_digit2):
        print("0")
    elif(r_digit1==g_digit3):
        print("0")
    elif(r_digit1==g_digit4):
        print("0")
    else:
        print(".")
    if(r_digit2==g_digit2):
        print("1")
    elif(r_digit2==g_digit1):
        print("0")
    elif(r_digit2==g_digit3):
        print("0")
    elif(r_digit2==g_digit4):
        print("0")
    else:
        print(".")
    if(r_digit3==g_digit3):
        print("1")
    elif(r_digit3==g_digit1):
        print("0")
    elif(r_digit3==g_digit2):
        print("0")
    elif(r_digit3==g_digit4):
        print("0")
    else:
        print(".")
    if(r_digit4==g_digit4):
        print("1")
    elif(r_digit4==g_digit1):
        print("0")
    elif(r_digit4==g_digit2):
        print("0")
    elif(r_digit4==g_digit3):
        print("0")
    else:
        print(".")
        
#Getting Output and Repeating The Game
    if(r_digit1==g_digit1 and r_digit2==g_digit2 and r_digit3==g_digit3 and r_digit4==g_digit4):
        print("CONGRATULATIONS! You WON The Game")
        question=input("Do You Want To Play Again (yes/no) ? ")
        if(question=="yes"):
            count=0
            r_digit1=random.randint(1,6)
            r_digit2=random.randint(1,6)
            r_digit3=random.randint(1,6)
            r_digit4=random.randint(1,6)
        else:
            print("Thank You For Playing The Game! See You Again")
            quit()
    count=count+1
    if(count==9):
        print("You LOST! Let's Try Again")
        question=input("Do You Want To Try Again (yes/no) ? ")
        if(question=="yes"):
            count=1
            r_digit1=random.randint(1,6)
            r_digit2=random.randint(1,6)
            r_digit3=random.randint(1,6)
            r_digit4=random.randint(1,6)
        else:
            print("Thank You For Playing The Game! See You Again")
            quit()
