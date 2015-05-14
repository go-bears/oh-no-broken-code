# This file has a few mistakes and some things I forgot to put in.
# When I run it I don't get anything... can you fix it so I
# get asked for my vacation spot, and get a recommendation?
# Hint:
# Start at the bottom and work upwards.

vacation_spots = ['New York','Mexico','Hawaii','Tahoe']

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


def best_vacation_spot():
#     # Look at the weather type and return the vacation spot that
#     # is the best for that weather.
#     # You can use this mapping:
    # snow = "Tahoe"
    # wind = "Hawaii"
    # rain = "New York"
    # sun = "Mexico"

    #return "Stay at home"

    destination_season = dict(zip(seasons, vacation_spots))
    return destination_season



# def vacation_activity():
# #     # Look up the vacation activity from activities
# #     # and return just the activity itself
# #     print activity

#     vacation_activity = {}
#     for weather in weather_patterns.keys():
#         vacation_activity[weather] = activities[weather_patterns[weather]]
#     print vacation_activity

def season_activity():
    #match season with best suited activity
    season_activity = {}

    for weather in weather_patterns.keys():
        season_activity[weather] = activities[weather_patterns[weather]]
    return season_activity

def get_my_vacation():

    season = raw_input("What season do you want to travel: spring, summer, fall or winter?")
    # check if season is in the seasons list
    # if season == True:
    #     for season in seasons:
    #         if not season in seasons:
    #             print "Sorry, that isn't a season. I can't help you."
        
    # else:
    #look up the weather type for that season
    for weather_type in weather_patterns.values():
        if season == weather_patterns.keys():
            weather_type = weather_patterns[season]
    return weather_type


    # get the best vacation spot for that type
    for vacation_spot in destination_season:
        if season == destination_season.keys():
            vacation_spot = destination_season[season]
    return vacation_spot

    # get the best vacation activity for that type
    for seasons in season_activity:
        if season == seasons:
            best_vacation = season_activity[seasons]
    return best_vacation
 
    print "You should travel to {}, where you can spend your time {}!".format(vacation_spot, best_vacation)


def main():
    print "Welcome to the Vacation-o-Matic!"

    get_my_vacation()
    season_activity()
    best_vacation_spot()

if __name__=="__main__":
    main()