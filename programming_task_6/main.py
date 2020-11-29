from order import Orders
from validation1 import *
from memento import Creator, Caretaker
def copying_of_orders(ls):
    ls1 = Orders()
    for i in ls.orders:
        ls1.add_to_list(i)
    return ls1


def memento(ls1: Orders, originator: Creator, caretaker: Caretaker):
    originator.change(ls1)
    caretaker.filling_stack()
    ls = originator.get_condition_o()
    return ls


ls = Orders()
file_name = validate_file_input()
ls.fill_list_from_file(file_name)
originator = Creator(ls)
caretaker = Caretaker(originator)
caretaker.filling_stack()
while True:
    userchoice = input('''welcome user choose your choice:
    1.) Search orders with value
    2.) Delete orders 
    3.) Add order
    4.) Print all orders
    5.) Undo
    6.) Redo
    7.)Exit''' + '\n')
    if userchoice == '1':
        val = input('Input value for order: ')
        ls.search_in_list(val)

    elif userchoice == '2':
        id =int(input('Input id: '))
        ls1 = copying_of_orders(ls)
        ls1.remove(file_name,id)
        ls = memento(ls1, originator, caretaker)
    elif userchoice == '3':
        new_order = input('Input info for new orders: ')
        if type(new_order) == str:
            ls1 = copying_of_orders(ls)
            ls1.add(new_order, file_name)
            ls = memento(ls1, originator, caretaker)
    elif userchoice == '4':
        if type(ls) == 'NoneType':
            print('Your orders_list is empty!')
        else:
            ls.print_list()
    elif userchoice == '5':
        caretaker.undo_redo('undo')
        ls = originator.get_condition_o()
        ls.rewrite_file(file_name)
    elif userchoice == '6':
        caretaker.undo_redo('redo')
        ls = originator.get_condition_o()
        ls.rewrite_file(file_name)
    elif userchoice == '7':
        print("thank fot using us !!!")
        break
    else:
        print('Wrong number of choice')