class MyIterator():

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        start_a, start_b = 0, 1

        while start_a < self.limit:
            print(start_a)
            if self.counter <= self.limit:
                start_a, start_b = start_b, start_a + start_b
                self.counter += 1
            else:
                raise StopIteration



class MyGenerator():

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def fib_generator(self):
        start_a, start_b = 0, 1
        while self.counter <= self.limit:
            yield start_a
            start_a, start_b = start_b, start_a + start_b
            self.counter += 1


