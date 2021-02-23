####Example given by instructor#####

class Base:
    def __init__(self):
        print('Base Intilizer')

    def f(self):
        print('Base.f()')


class Sub(Base):
    def __init__(self):
        super().__init__()
        print('Sub Intilizer')

    def f(self):
        print('Sub.f()')


#####################Self made example###################3

class Bird:
    def __init__(self,color):
        self.color = color


    def topspeed(self):
        avg_speed = [10,40,34,54]
        topspeed = max(avg_speed)
        return topspeed

    def print_color(self,color):
        print(color)



class Tucan(Bird):

    def __init__(self,color):
        self.color = color

    def topspeed(self):
        avg_speed = [10,20,30,40,50]
        func = lambda x: x + 1
        top_speed = max(map(func,avg_speed))
        print(top_speed)


base = Base()
base.f()
sub = Sub()
sub.f()