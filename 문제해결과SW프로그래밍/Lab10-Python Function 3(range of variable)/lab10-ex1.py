seconds_per_minute = 60

def minutes_to_seconds(minutes):
    seconds = minutes*seconds_per_minute
    return seconds

seconds = minutes_to_seconds(3)
print(seconds)
