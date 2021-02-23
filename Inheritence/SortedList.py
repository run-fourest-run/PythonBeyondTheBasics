class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "SimpleList({!r})".format(self._items)


class SortedList(SimpleList):
    def __init__(self, items=()):
        super(SortedList, self).__init__(items)
        self.sort()

    def add(self, item):
        super.add(item)
        self.sort()

    def __repr__(self):
        return "SortedList({!r})".format(list(self))


###Type checking an object using inhereitence

class IntList(SimpleList):
    def __init__(self,items=()):
        for x in items: self._validate(x)
        super().__init__(items)



    @staticmethod
    def _validate(x):
        if not isinstance(x,int):
            raise TypeError('IntLists only support integer vals')

    def add(self,item):
        self._validate(item)
        super().add(item)

    def __repr__(self):
        return "Class IntList({!r})".format(list(self))

##type checked lists
intlist = IntList([1,2,3,4,5,6])
failedintlist = IntList([1,2,3,"string"])
# Instantiating Simple List and Sorted List
simple_list = SimpleList([2, 4, 5, -234, 24, 52, 522])
sl = SortedList([2, 4, 5, -234, 24, 52, 522])


# isinsance() determines if an object is of a specified type
# use isintance() for runtime type checking
# Returns true or false -- boolean test
# Returns True if object is a subclass of second arguement
print(isinstance(2, int))
print(isinstance(2, str))
print(isinstance(2, float))

# You can see s1 is an instance of both the Parent and the Subclass
print(isinstance(sl, SimpleList))
print(isinstance(sl, SortedList))
print("is Simple List of type Sorted List: {}".format(isinstance(simple_list,SortedList)))
print("is Sorted List of type Simple List: {}".format(isinstance(sl,SimpleList)))

# you can also pass a tuple to the second arguement to check if the object belongs to any of the types in the Tuple.
print(isinstance("str", (str, int, SimpleList)))
print(isinstance(44, (str, int, SimpleList)))
print(isinstance(sl, (SimpleList, int)))
