from datetime import datetime

number_endings = {
1: 'st',
2: 'nd',
3: 'rd'
}


today = datetime.now()
todays_day = today.day
# get the right ending, e.g. 1 => 1st, 2 => 2nd
# but beware! 11 => 11th, 21 => 21st, 31 => 31st
# test your code by forcing todays_day to be something different
ending = 'th'

if todays_day < 10:
# x % y (mod) will give the remainder when x is divided by y
# -- but x needs to be an intHeger!
	number = int(todays_day)
# look up number in number_endings
	if number ==1:
		print "Today is the {}{}".format(number, number_endings[1])
	elif number == 2:
		print "Today is the {}{}".format(number, number_endings[2])
	elif number == 3:
		print "Today is the {}{}".format(number, number_endings[3])
	else:
		print "Today is the {}{}".format(todays_day, ending)

elif todays_day > 20:
	number = int(todays_day)
	if number == 21 or 31:
		print "Today is the {}{}".format(number, number_endings[1])
	elif number == 22:
		print "Today is the {}{}".format(number, number_endings[2])
	elif number == 23:
		print "Today is the {}{}".format(number, number_endings[3])
	else:
		print "Today is the {}{}".format(todays_day, ending)

else:
	print "Today is the {}{}".format(todays_day, ending)




# and if you find it as a key, put the value in ending
#		if number in number_endings:

#make this print ending, not 'th'
	print "Today is the {}{}".format(todays_day, ending)


birthday = int(raw_input("What day of the month is your birthday?"))
# make this print the birthday, and the right ending
number = int(birthday % 10)
print number

if birthday < 10:
	number = int(birthday % 10)
	print number
# x % y (mod) will give the remainder when x is divided by y
# -- but x needs to be an integer!
# look up number in number_endings
	if birthday ==1:
		print "Your birthday is the {}{}".format(birthday, number_endings[1])
	elif birthday == 2:
		print "Your birthday is the {}{}".format(birthday, number_endings[2])
	elif birthday == 3:
		print "Your birthday is the {}{}".format(birthday, number_endings[3])
	else:
		print "Your birthday is the {}{}".format(todays_day, ending)

if birthday >= 20:
	if birthday == 21 or 31:
		print "Your birthday is the {}{}".format(birthday, number_endings[1])
	elif birthday == 22:
		print "Your birthday is the {}{}".format(birthday, number_endings[2])
	elif birthday == 23:
		print "Your birthday is the {}{}".format(birthday, number_endings[3])
	else:
		print "Your birthday is the {}{}".format(birthday, ending)

else:
	print "Your birthday is on the {}th!".format(birthday)