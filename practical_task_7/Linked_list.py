from logger_class import Event
from function import isPrime
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    event = Event()
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(nodes[0])
            self.head = node
            for elem in range(1, len(nodes)):
                node.next = Node(nodes[elem])
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def length_of_linked_list(self):
        k = 0
        for node in self:
            k += 1
        return k

    def push_back(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node

    def pop_node(self, pos,param=None):
        current_node = self.head
        deleted_node = self.head
        prev = 0
        if current_node is not None:
            if pos == 1:
                if param == 'get':
                    return deleted_node
                else:
                    self.head = current_node.next
                    self.event.notify('delete', deleted_node, pos, self.str_format())
                    return
        k = 0
        while current_node is not None:
            k += 1
            if k == pos:
                deleted_node = current_node
                if param == 'get':
                    return deleted_node
                else:
                    break
            prev = current_node
            current_node = current_node.next
        prev.next = current_node.next
        if param is None:
            print('!')
            self.event.notify('delete', deleted_node, pos, self.str_format())

    def pop_nodes_in_range_mode(self, pos1, pos2):
        if pos1 > pos2:
            pos1, pos2 = pos2, pos1
        k = 0
        l = pos2 - pos1 + 1
        deleted_list = []
        for node in self:
            k += 1
            if k <= l:
                deleted_list.append(self.pop_node(pos1, 'get'))
                self.pop_node(pos1, 'remove')
        self.event.notify('delete', deleted_list, pos1, pos2, self.str_format())

    def insert_node(self, pos, new_data):
        k = 1
        current_node = self.head
        if k == pos:
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node
            return
        for node in self:
            k += 1
            if k == pos:
                current_node = node
        new_node = Node(new_data)
        new_node.next = current_node.next
        current_node.next = new_node
    def insert_in_the_list(self, pos, ls):
        if self.length_of_linked_list() != 0 or pos < self.length_of_linked_list():
            for i, elem in enumerate(ls):
                self.insert_node(pos + i, elem)
        else:
            for i in ls:
                self.push_back(i)
        self.event.notify('add', ls, pos, self.str_format())

    def print_list(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes = list(map(str, nodes))
        return " ".join(nodes)

    def str_format(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes = list(map(str, nodes))
        return " ".join(nodes)

    def countPrime(self):

        count = 0
        ptr = self.head

        while ptr != None:


            if isPrime(ptr.data):

                count += 1

            ptr = ptr.next

        return count