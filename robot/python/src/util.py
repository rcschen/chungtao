import time
import datetime

def get_duration_timestamp(lastTimestamp):
    nowTimestamp = time.time()
    nowSecond = datetime.datetime.fromtimestamp( nowTimestamp ).second
    lastSecond = datetime.datetime.fromtimestamp( lastTimestamp ).second
    if lastSecond > nowSecond:
       nowSecond += 60
    duration = nowSecond - lastSecond
    return duration, nowTimestamp

def get_diff_timestamp(lastTimestamp):
    nowTimestamp = time.time()
    nowSecond = datetime.datetime.fromtimestamp( nowTimestamp ).second
    lastSecond = datetime.datetime.fromtimestamp( lastTimestamp ).second
    diff = nowTimestamp - lastTimestamp

    #if lastSecond > nowSecond:
       #nowSecond += 60
    #duration = nowSecond - lastSecond

    #if duration == 1:
       #print diff       
       #print "duration:", duration
    return diff, nowTimestamp

