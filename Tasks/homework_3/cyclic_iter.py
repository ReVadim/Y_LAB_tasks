class CyclicIterator:
    """ Infinite cyclic iterator
    """
    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self
        except StopIteration:
            return self


a = [0, 1, 2, 3]

itr = CyclicIterator()
print(itr)
