import random
import datetime
import itertools
import time
import psutil
import pyowm
import geocoder



class Sensor:
    def __iter__(self):
        return self

    def __next__(self):
        mylocation = geocoder.ip('me')
        latlong = mylocation.latlng
        omw = pyowm.OWM('1bfbe76e150ede97d065c9304b1958e0')
        return omw.weather_manager().weather_at_coords(latlong[0],latlong[-1])

sensor = Sensor()
timestamps = iter(datetime.datetime.now,None)



for stamp, value in itertools.islice(zip(timestamps,sensor),10):
    print(stamp,value)
    time.sleep(1)


