import reprlib
import datetime

class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z =z

    def __str__(self):
        return 'Point3D({},{},{})'.format(self.x,self.y,self.z)

    def __repr__(self):
        return '(x={},y={},z={})'.format(self.x,self.y,self.z)

# Repr is written for Developers - It means representation and is best used for debugging
# Str is written by Customers - It is supposed to encompass all attributes


day = datetime.date.today()



d = datetime.date.today()
a  = datetime.datetime.now()
b = datetime.datetime(year=2020, month=6,day=5)
c = b -a