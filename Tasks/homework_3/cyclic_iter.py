test_list = [0, 1, 2, 3]


class CyclicIterator:
    """ Infinite cyclic iterator
    """
    def __init__(self, value):
        self.value = value
        self.iterator = iter(value)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.value)
            return next(self.iterator)


for x in CyclicIterator(test_list):
    print(x)
