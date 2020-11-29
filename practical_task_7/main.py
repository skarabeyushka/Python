import threading
from Linked_list import LinkedList
from validation import *
from logger_class import *
from context import Context
from threading import Thread


class Object:

    def __init__(self, li, size=2):
        self.arguments = li
        self.size = size

    def get_list_for_each(self):
        result = []
        c = len(self.arguments) // self.size
        for i in range(0, len(self.arguments), c):
            a = []
            for j in range(i, i + c):
                a.append(self.arguments[j])
            result.append(a)
        return result


def create_thread(li_of_funcs, obj: Object):
    args1 = obj.get_list_for_each()
    current_threads = []
    for i in range(len(li_of_funcs)):
        thread = threading.Thread(target=li_of_funcs[i], args=(*args1[i],))
        thread.start()
        current_threads.append(thread)
    for i in range(len(current_threads)):
        current_threads[i].join()


def create_first_strategy(linked_list: LinkedList):
    n = validate_input('quantity of elements in list ')
    a = validate_input('left_border', linked_list.length_of_linked_list())
    b = validate_input('right_border', linked_list.length_of_linked_list())
    pos = validate_input('position to start ', linked_list.length_of_linked_list())
    linked_list = context.do(linked_list, n, a, b, pos)
    return linked_list


def create_second_strategy(linked_list: LinkedList):
    pos = validate_input('position', linked_list.length_of_linked_list())
    file_name = validate_file_input()
    linked_list = context.do(linked_list, pos, file_name)
    return linked_list


linked_list_first = LinkedList()
linked_list_second = LinkedList()

linked_list_first.event.add(Observer('add', Logger.write_to_file))
linked_list_first.event.add(Observer('delete', Logger.write_to_file))

linked_list_second.event.add(Observer('add', Logger.write_to_file))
linked_list_second.event.add(Observer('delete', Logger.write_to_file))

context = Context(1)

print(' linked_list_first: ')
linked_list_first = create_first_strategy(linked_list_first)
context.change_strategy(2)
print('linked_list_second: ')
linked_list_second = create_second_strategy(linked_list_second)


def countprimeee(linked_list: LinkedList):
    linked_list.countPrime()



while True:
    print('''Choose option:
    1.)first Strategy for adding in list
    2.) second Strategy for adding in list
    3.) Generating data for the list 
    4.) Delete element by position
    5.) Delete range of elements
    6.) count prime numbers
    7.) Print list
    8. Exit
    ''')
    userchoice = validate_input('userchoice')
    if userchoice == 1:
        context.change_strategy(1)
    elif userchoice == 2:
        context.change_strategy(2)
    elif userchoice == 3:
        if context.get_strategy() == 1:
            print('first list: ')
            linked_list_first = create_first_strategy(linked_list_first)
            print(' second list')
            linked_list_second = create_first_strategy(linked_list_second)
        elif context.get_strategy() == 2:
            print(' first list: ')
            linked_list_first = create_second_strategy(linked_list_first)
            print(' second list')
            linked_list_2 = create_second_strategy(linked_list_second)
    elif userchoice == 4:
        pos1 = validate_input('position for the first list', linked_list_first.length_of_linked_list(), 'delete')
        pos2 = validate_input('position for the second list', linked_list_second.length_of_linked_list(), 'delete')
        create_thread([linked_list_first.pop_node, linked_list_second.pop_node], Object([pos1, pos2]))
    elif userchoice == 5:
        pos1first = validate_input('start_pos for the first list', linked_list_first.length_of_linked_list())
        pos2first= validate_input('end_pos for the first list', linked_list_first.length_of_linked_list())

        pos1second = validate_input('start_pos for the second list', linked_list_second.length_of_linked_list())
        pos2second = validate_input('end_pos for the second list', linked_list_second.length_of_linked_list())

        create_thread([linked_list_first.pop_nodes_in_range_mode, linked_list_second.pop_nodes_in_range_mode], Object([pos1first, pos2first, pos1second, pos2second]))
    elif userchoice == 6:
        p1 = linked_list_first.countPrime()
        p2 = linked_list_second.countPrime()
        print("prime numbers for the first list is =",p1)
        print("prime numbers for the second list is =", p2)

    elif userchoice == 7:
        print(linked_list_first.str_format())
        print(linked_list_second.str_format())
    elif userchoice == 8:
        f = open('output1.txt', 'r+')
        f.truncate(0)
        break