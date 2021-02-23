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


print("IntList is a subclass of SimpleList: {}".format(issubclass(IntList,SimpleList)))
print("SimpleList is a subclass of IntList: {}".format(issubclass(SimpleList,IntList)))