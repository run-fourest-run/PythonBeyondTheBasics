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
        return psutil.virtual_memory()

sensor = Sensor()
timestamps = iter(datetime.datetime.now,None)



for stamp, value in itertools.islice(zip(timestamps,sensor),10):
    print(stamp,value)
    time.sleep(1)



