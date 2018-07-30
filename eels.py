# This is a practice exercise for Codecademy on the Rock Paper Scissor Module

# this imports randomint from random
from random import randint

#This will define the options in a key for the computer and user to select [] for list

options = ["EELS", "ESCALATORS"]

# This index will provide the program with the different messages it will tell the user {} for index remember a comma after the end of each string
# Remember to close the curly braces at the end of an index
import time
messages = {
	"down": "Looks like you got %s!" % options[0].lower() +  """
	Down
	Down
	Down!""",
	
	"up": "Looks like you got %s!" % options[1].lower() + """
	Up
	UP
	AND AWAY!""",
	
	"down1": "Looks like the computer got %s!" % options[0].lower() +  """
	Down
	Down
	Down!""",
	
	"up1": "Looks like the computer got %s!" % options[1].lower() + """
	Up
	UP
	AND AWAY!""",
	}
# This will define a function that will tell what you got vs the computer
def choice(user_choice, computer_choice):
	print "You chose %s!" % user_choice.lower()
	if user_choice == options[1]:
		print messages["up"]
		time.sleep(1)
		print
	else:
		print messages["down"]
		time.sleep(1)
		print
		
	print "The computer chose %s" % computer_choice.lower()
	if computer_choice == options[1]:
		print messages["up1"]
		time.sleep(1)
		print
	else:
		print messages["down1"]
		time.sleep(1)
		print 
	if user_choice == computer_choice:
		print "You both got %s!" % user_choice.lower()
	elif user_choice != computer_choice:
		print "You got %s!" % user_choice + " The computer got %s!" % computer_choice.lower()
	print 
	print "Play again?"
	yn = raw_input("Enter yes or no: ").upper()
	if yn == "YES":
		print "Excellent!"
		return play()
	else:
		print "Thanks for playing!"
		time.sleep(1)

# This function will play the game
def play():
	user_choice = raw_input("Enter eels or escalators!: ").upper()
	computer_choice = options[randint(0, 1)]
	choice(user_choice, computer_choice)

name = raw_input("Enter name: ")
print "Starting......"
time.sleep(2)
print
print
print "~Welcome to Eels and Escalators, %s!~" % name
print
play()

