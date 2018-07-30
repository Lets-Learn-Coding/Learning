#This is a tip calculator for codecademy
def tip():
	print "Hi I'm a tip calc!"
	print "Enter the price of your meal!"
	meal = input("Price of Meal: ")
	print "$" + str(meal) + " yum!"
	print "How much tax?"
	perctax = input("%: ")
	print str(perctax) + "% tax"
	tax = perctax / 100
	mealtax = meal + meal * tax
	print "$" + str(mealtax) + " with tax!" 
	print "How much would you like to tip?"
	tipperc = input("%: ")
	print str(tipperc) + "% tip"
	tip = tipperc / 100.0
	mealtip = meal * tip
	print "Your tip is $" + str(mealtip)
	total = mealtax + mealtip
	print "Your total bill is $" + str(total)
	print """
	THANK
	YOU
	VERY
	MUCH"""
	yn = raw_input("work?: ")
	
	
tip()
	