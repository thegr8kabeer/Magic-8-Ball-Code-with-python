# Magic 8-Ball made by the Thegr8kabeer
# Follow me on GitHub at https://github.com/thegr8kabeer
# Simple code for beginners to understand the syntax
# Follow me on instagram at https://www.instagram.com/thegr8kabeer/


# Importing the modules
import sys

# For generating random answers
import random

# Setting the user input in the variable 'answer'

# Checking for valid answer
answer = True

while answer:
    question = input("Ask the magic 8 ball a question:\n(press enter to get the answer): ")
    
    answers = random.randint(1,8)
    
    # if the answer of the user is null, the program will exit itself.
    if question == "":
        sys.exit()
    
    # Otherwise it will proceed
    elif answers == 1:
        print ("It is certain")
    
    elif answers == 2:
        print ("Outlook good")
    
    elif answers == 3:
        print ("You may rely on it")
    
    elif answers == 4:
        print ("Ask again later")
    
    elif answers == 5:
        print ("Concentrate and ask again")
    
    elif answers == 6:
        print ("Reply hazy, try again")
    
    elif answers == 7:
        print ("My reply is no")
    
    elif answers == 8:
        print ("My sources say no")

# feel free to edit my code by adding more lines of code
# Happy Coding!
# Don't forget to follow!!!