# This is a syntax review exercise from codecademy
def avg():
	print "Lets determine your points!"
	print "How many activities have you completed?"
	act = input("Activities: ")
	print str(act) + " Activities!"
	print "How many points per activity?"
	points = input("Points Per: ")
	print "Any extra credit points?"
	extra = input("ExtraCred: ")
	print str(extra) + " Extra Credit Points!"
	total = int(act) * int(points) + int(extra)
	print "Your total points is " + str(total) + "!"
	yn = raw_input("work?: ")

avg()