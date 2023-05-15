import datetime
def time_shift(time,minutes):
    time = datetime.datetime.strptime(time,"%X")
    extratime = datetime.timedelta(minutes = minutes)
    time_new = time - extratime
    print(time_new)

time_shift("09:00:00",15)
