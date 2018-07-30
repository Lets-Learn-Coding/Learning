# Hello I am a Pizza Splitter
def pizza():
	print "Hello, how many pizzas would you like?"
	pizzas = input("This many: ")
	print pizzas, " it is!"
	print "How many people?"
	people = input("This many: ")
	print "So, ", pizzas, " pizzas and ", people, " people!"
	print "Should we slice them equally?"
	total_pieces = pizzas / float(people)
	divide = raw_input("y/n: ")
	if divide == "y":
		print total_pieces, "pieces per person it is!"
		print "Enjoy Your Meal"
		return
	elif divide == "n":
		print "Enjoy your meal!"
		
	yn = raw_input("work?: ")
	
pizza()