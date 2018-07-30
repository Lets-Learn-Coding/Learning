# This is practice concatenation!
def practice():
	print "This" + " is" + " practice" + " con" + "cat" + "en" + "at" + "ion" + " for" + " codecademy!"
# when concatenating numbers its best to define them as a variable and then use str() for calling
	number = 2018.1
	print str(number) + " is a number!"
# String Formatting with % is trickier
# Define the variables for the strings that you want to call
	var1 = "Nic"
	print "Hello %s" % (var1)
	var2 = "pizza"
	print "Hey %s! Want some %s?" % (var1, var2) 
# Sometimes its important to pad integer variables %02d means
# 0- pad with zeroes        2- 2 Characters wide      d- integer can be negative or positive
	day = 22
	month = 7
	year = 2018
	print "%s - %02d - %s" % (month, day, year) + " is the date I was born!"
# You can also take raw input strings and have them appear as well after they're declared as variables
	name = raw_input("My name is: ")
	age = raw_input("How old are you? ")
	place = raw_input("Where are you from? ")
	food = raw_input("What do you like to eat? ")
	print "Oh! So your name is %s, you're %s years old, you live in %s, and your favorite food is %s!" % (name, age, place, food)
	yn = raw_input("work?: ")

	
practice()
