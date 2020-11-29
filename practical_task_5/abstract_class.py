from classstrategy import *

class Abstract_Class:
    def __init__(self, n):
        self.strategy = n

    def choose_strategy(self, n):
        self.strategy = n

    def do(self, *args):
        if self.strategy == 1:
            s = Strategyfirst(*args)
        else:
            s = Strategysecond(*args)
        return s.func()

    def return_strategy_number(self):
        return self.strategy