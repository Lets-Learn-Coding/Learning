#Practicing indexes Codecademy 
# [] after a string will show that character
def bingo():
	print "BINGO"
	word = "bingo"
# len(*variable*) will show the length/amount of characters that a string is 	
	word1 = len(word)
	first_letter = "BINGO"[0]
	print "The first letter of BINGO is " + str(first_letter)
	print "When using indexes the first letter of a string is always 0"
	
	third_letter = "BINGO"[2]
	print "The third letter of BINGO is " + str(third_letter)
	print "This letter is the third, but its index is 2"
# len(*variable*) will show the length/amount of characters that a string is 
	print "Bingo is " + str(word1) + " characters long"
# variable.lower() makes the string lower case!
	print word.lower() + " is the .lower() form of BINGO!"
# variable.upper() makes the string upper case!
	print word.upper() + " is the .upper() form of bingo!"

bingo()
yn = raw_input("...")