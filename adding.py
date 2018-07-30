
""" Welcome Sequence """
print "Welcome to Addition Basics!"
name = raw_input("Please Enter Your Name: ")
print "Welcome " + name + "!"
print "Please enter 'yes' or 'no'"
word2 = raw_input("Ready to do some MATH?: ").upper()	

""" Addition Function"""
def adding():
	print "Welcome to Addition %s!" % name
	print "What is value A?: "
	valA = input("A: ")
	print "What is value B?: "
	valB = input("B: ")
	total = valA + valB
	print name + ", your value for " + str(valA) + " and " + str(valB) + " is " + str(total) + "!"
	pa = raw_input("Play Again?: ").upper()
	if pa.lower() == "YES":
		print "Yay!"
		return adding()
	else:
		print "Goodbye."

""" Takes input for word2 """
if word2 == "YES":
	print "Excellent"
	adding()
else:
	word2 != "YES"
	print " :( "
	word3 = raw_input("Are you sure?: ").upper()
	
""" Are you sure? """
if word3 == "YES":
	print "Let's get to it "+ name + "!"
	adding()
else:
	word3 != "NO"
	print "Bye"
	


