# Import from datetime with 
# from datetime import datetime
from datetime import datetime

# Show what date/time it is right now! datetime.now()
print str(datetime.now()) + " This is in datetime.now() form"
now = datetime.now()
print str(now) + " This is in variable form!"

# use .year .month .day to show the year month and day!
year = now.year
month = now.month
day = now.day

# Use indexes to call the year month and date declare number of digits %02d %04d 2d for 2 4d for 4
print "This is a cleaned up date using indexes! " + "%02d/%02d/%04d" % (month, day, year) 

# You can also print the hour, minute, and second .hour .minute .second
print "The time is " + "%02d:%02d:%02d" % (now.hour, now.minute, now.second)

# You can also print it all together with indexes!
print "%02d/%02d/%04d   %02d:%02d:%02d" % (now.month, now.day, now.year, now.hour, now.minute, now.second)
yn = raw_input(" I am a placeholder, type to exit")