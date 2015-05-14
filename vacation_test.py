# This file has a few mistakes and some things I forgot to put in.
# When I run it I don't get anything... can you fix it so I
# get asked for my vacation spot, and get a recommendation?
# Hint:
# Start at the bottom and work upwards.


vacation_spots = ['New York', 'Mexico', 'Hawaii', 'Tahoe', ]

seasons = ['spring', 'summer', 'fall', 'winter']

weather_patterns = {
    'spring': 'rain',
    'summer': 'sun',
    'fall': 'wind',
    'winter': 'snow'
}

activities = {
    'rain': 'visiting museums',
    'wind': 'kiteboarding',
    'sun': 'sunbathing',
    'snow': 'skiing'
}



destination_season = dict(zip(seasons, vacation_spots))
#print destination_season


vacation_activity = {}
for weather in weather_patterns.keys():
    vacation_activity[weather] = activities[weather_patterns[weather]]

#print vacation_activity


season = raw_input("What season do you want to travel: spring, summer, fall or winter?")

for seasons in destination_season:
    if season == seasons:
        vacation_spot = destination_season[seasons]
        #print vacation_spot

for seasons in vacation_activity:
    if season == seasons:
        best_vacation = vacation_activity[seasons]
        #print best_vacation

print "You should travel to {}, where you can spend your time {}!".format(vacation_spot, best_vacation)