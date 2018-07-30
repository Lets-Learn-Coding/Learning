print "Welcome to MadLibs!"
# Get global variables for *story*
name = raw_input("Enter name: ")
print "Nice name!"
job = raw_input("Enter job: ")
print "That\'s a good one!"
adjective = raw_input("Enter Describing Word: ")
print "Interesting choice..."
food = raw_input("Enter a delicious food: ")
print "Yum!"
print "Ready to read the story?"
# The story variable holds the story along with string replacements
story = "%s woke up from a long nap. Its not easy for a %s nowadays. The day was very %s . %s looked up, was raining %ss!" % (name, job, adjective, name, food)

# This function is a yes or no checker
def start():
	qa = raw_input("Start?: ")
	if qa == "yes":
		print "Let\'s get started!"
		print story
	else:
		print "That\'s too bad!"
		
def check():
	yn = raw_input("Did it work: ")
	if yn == "yes":
		print "HOORAY!"
	else:
		print "Try again!"

start()
check()
