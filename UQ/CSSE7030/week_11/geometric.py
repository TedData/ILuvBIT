class GeometricSequence(object) :
    """A geometric sequence of numbers.

    The sequence of numbers:
    start, start * ratio, start * ratio**2, ..., start * ratio**(length-1)
    Without a length parameter, the sequence is infinite.
    """

    def __init__(self, start, ratio, length=None) :
        self._start = start
        self._ratio = ratio
        self._len = length

    def __iter__(self) :
        return GeometricIterator(self._start, self._ratio, self._len)


class GeometricIterator(object) :
    """An iterator on a geometric sequence."""

    def __init__(self, start, ratio, length) :
        # Store values for later
        self._ratio = ratio
        self._len = length
        # Store information about position in the sequence
        self._pos = 0
        self._value = start

    def __iter__(self) :
        return self

    def __next__(self) :
        # Check if the sequence has finished
        if self._len is not None and self._pos >= self._len :
            raise StopIteration
        tmp = self._value
        # Update for next time.
        self._value *= self._ratio
        self._pos += 1
        return tmp


if __name__ == "__main__" :
    print("EXAMPLE 1:")

    powers_two = GeometricSequence(1, 2)

    it = iter(powers_two)
    print(next(it), next(it), next(it), next(it))  # 1 2 4 8

    # Find the first number in the sequence bigger than 1000.
    for x in powers_two :
        if x > 1000 :
            print(x, "is bigger than 1000.")
            break


    print()
    print("EXAMPLE 2:")

    seq = GeometricSequence(2, 3, 6)  # 2, 6, 18, 54, 162, 486
    for x in seq:
        print(x,)
    print("Stop.")

    print("Is 54 in the sequence?", 54 in seq)
    print("Is 20 in the sequence?", 20 in seq)

    print()
    print("EXAMPLE 3:")
    string_sequence = GeometricSequence('*', 2, 4)
    print(' '.join(string_sequence))
