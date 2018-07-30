# Testing Functions
def double(a):
	result = a * 2
	print str(a) + " doubled is " + str(result) + "!"
def triple(a):
	result = a * 3
	print str(a) + " tripled is " + str(result) + "!"
	
#Intro code defining a 	
a = input("What to double?: ")
double(a)
print "Would you like to triple " + str(a) + "?"
yn = raw_input("y/n: ")
if yn == "y":
	triple(a)
elif yn == "n":
	print "Thanks for playing!"