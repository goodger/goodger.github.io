class C:

    i = 0
        
    def next(self):
        self.i += 1
        return self.i

    def __iter__(self):
        return self


class MyRangeClass:

    """1-argument 'range' equivalent."""

    def __init__(self, stop):
        self.stop = stop
        self.value = 0

    def __iter__(self):
        # Must return an object with a "next" method.
        # Usually just returns self (self.next must exist).
        return self

    def next(self):
        # Return the next value, or raise StopIteration.
        if self.value >= self.stop:
            raise StopIteration
        value = self.value
        self.value += 1
        return value


def my_range_generator(stop):
    value = 0
    while value < stop:
        yield value
        value += 1


def _linewise_generator(data_file):
    # Uses file.readline to keep the file position in sync.
    # "for line in file" gets out of sync.
    while 1:
        line = data_file.readline()
        if line:
            yield line
        else:
            break

def _decoded_generator(self, source):
    for row in source:
        yield [entry.decode('latin-1') for entry in row]
