from startegymetthodes import firstStrategy, secondStrategy


class Context:
    def __init__(self, num):
        self.strategy = num

    def change_strategy(self, num):
        self.strategy = num

    def do(self, *args):
        if self.strategy == 1:
            e = firstStrategy(*args)
        else:
            e = secondStrategy(*args)
        return e.method()

    def get_strategy(self):
        return self.strategy