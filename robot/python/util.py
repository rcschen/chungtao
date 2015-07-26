import time
import datetime

def get_duration_timestamp(lastTimestamp):
    nowTimeStamp = time.time()
    nowSecond = datetime.datetime.fromtimestamp( time.time() ).second
    lastSecond = datetime.datetime.fromtimestamp( lastTimestamp ).second
    if lastSecond > nowSecond:
       nowSecond += 60
    duration = nowSecond - lastSecond
  
    #if duration >=2: 
       #print "duration",duration
 
    return duration, nowTimeStamp

