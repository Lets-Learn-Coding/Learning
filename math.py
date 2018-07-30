# This is a price calculator
def ppd():
	dogs = input("How many dogs?: ")
	price_per_dogs = 350
	total = dogs * price_per_dogs
	print total
	print "did it work?"
	yn = raw_input("?: ")

def ppa():
	a = input("How many alligators?: ")
	price_per_alligators = 200
	total = a * price_per_alligators
	print total
	print "did it work?"
	yn = raw_input("?: ")
	
ppd()
ppa()