from linked_list import LinkedList
from  iterator import making_sequence_number
from abc import ABCMeta,abstractmethod

class Strategy(metaclass=ABCMeta):

    @abstractmethod
    def func(self):
        pass

class Strategyfirst(Strategy):

    def __init__(self, ll: LinkedList, n, a, b, pos):
        self.ll = ll
        self.n = n
        self.a = a
        self.b = b
        self.pos = pos

    def func(self):
        ls = making_sequence_number(self.a, self.b, self.n)
        self.ll.insert_in_the_list(self.pos, ls)
        return self.ll


class Strategysecond(Strategy):

    def __init__(self, ll: LinkedList, pos, file_name):
        self.ll = ll
        self.pos = pos
        self.file_name = file_name

    def func(self):
        f = open(self.file_name, 'r')
        ls = [int(i) for i in ''.join(f.readlines()).split()]
        self.ll.insert_in_the_list(self.pos, ls)
        return self.ll