from random import randint

class Negative(Exception):
    pass
def user_input(givenchoice):
    while True:
        try:
            if givenchoice == "linked_list":
                choice = [int(i) for i in input("Input linked list: ").split()]
                for i in choice:
                    if str(abs(i)).isnumeric() is False:
                        raise ValueError
            elif givenchoice == "a" or givenchoice == "b":
                choice = int(input('Input ' + givenchoice + ': '))
                if str(abs(choice)).isnumeric() is False:
                    raise ValueError
            else:
                choice = int(input('Input ' + givenchoice + ': '))
                if choice < 0:
                    raise Negative
        except Negative:
            print(givenchoice + " should be positive")
        except ValueError:
            print("You typed not a number")
        else:
            return choice


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self, n=None):
        self.head = None
        if n is not None:
            node = Node(n[0])
            self.head = node
            for elem in range(1, len(n)):
                node.next = Node(n[elem])
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def push_back(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node

    def __repr__(self):
        node = self.head
        n = []
        while node is not None:
            n.append(node.data)
            node = node.next
        n = list(map(str, n))
        return " ".join(n)



    def search(self, x):

         sum = 0

         current = self.head


         while current != None:
            if current.data == x:
                sum=+1
            current = current.next
         return sum

    def find_index(self, key):
        return self.find_index_helper(key, 0, self.head)

    def find_index_helper(self, key, start, node):
        if node is None:
            return -1

        if node.data == key:
            return start
        else:
            return self.find_index_helper(key, start + 1, node.next)

    def largestElement(self, x):
        sum=0
        n = self.head
        max= n.data




        


        while (n != None):

            if (max < n.data):
                max = n.data
            n = n.next

        if(max==x):
            sum+=1
            print("k is max ")
        else:
            print("k is not max")
            sum+=0
        return sum

    def ispositive(self):
        sum=0

        n = self.head

        while (n != None):
            if (n.data > 0):
                sum+=1

            n = n.next
        return sum

    def replace(self, index):

        n = self.head
        for i in range(0,index):
            n.data=(n.data)**3
            n=n.next



while True:
    print('''welcome user !!!!
    Choose your option: 
    1. Input linked list elemnets and k 
    2. Input n, k and the linked list will be generated randomly
    3. Exit''')
    userchoice = user_input("your choice")
    if userchoice == 1:
        linked_list = LinkedList(user_input("linked_list"))
        linked_list1 = LinkedList(user_input("linked_list"))
        k = user_input("k")
        print("linked list x :",linked_list.__repr__())
        print("linked list y :",linked_list1.__repr__())
    elif userchoice == 2:
        n = user_input("n")
        print("You need to input a i b for range of elements: ")
        a = user_input("a")
        b = user_input("b")
        k = user_input("k")
        linked_list = LinkedList([randint(a, b) for i in range(n)])
        linked_list1 = LinkedList([randint(a, b) for i in range(n)])
        print("linked list x :",linked_list.__repr__() )
        print("linked list  y :",linked_list1.__repr__())

    else:
        print("thank you for your time!!!!!")
        break

    linked_list.largestElement(k)
    if (linked_list.search(k) == 1):
        print("k is in linked list x")
    else:
        print("k is not in linked list x")
    if (linked_list1.ispositive() == 0):
        print("linked list y is  negative ")
    else:
        print("linked list y is not  negative ")

    sum = 0;
    index = linked_list.find_index(k)
    sum = linked_list.largestElement(k) + linked_list.search(k) + linked_list1.ispositive()
    if (sum == 2):
        linked_list.replace(index)
        print(linked_list.__repr__())

