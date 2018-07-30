# This is a practice for Codecademy using functions
def gymcost():
	months = input("How many months will you workout?: ")
	type = raw_input("Charter or LA: ").upper()
	if type == "LA":
		cost = 25 * months
		print "Your cost for " + str(months) + " months of membership at " + str(type) + " will be $" + str(cost) + "."
	elif type == "CHARTER":
		cost = 10 * months
		print "Your cost for " + str(months) + " months of membership at " + str(type) + " will be $" + str(cost) + "."
		
def yn():
	yn = raw_input("Enter again? (y/n): ")
	if yn == "y":
		return gymcost()
	elif yn == "n":
		print "Thanks for using Gym Cost!"
	
			

gymcost()
yn()