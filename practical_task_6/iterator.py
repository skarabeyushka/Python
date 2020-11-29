from random import randint


class randomnumber:
    def __init__(self, n, a, b):
        self.limit = n
        self.counter = 0
        self.left = a
        self.right = b

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return randint(self.left, self.right)
        else:
            raise StopIteration

    def __iter__(self):
        return self


def making_sequence_number(w, e, n):
    if w > e:
        w, e = w, e
    li = []
    f = randomnumber(n, w, e)
    for i in range(n):
        li.append(next(f))
    return li
