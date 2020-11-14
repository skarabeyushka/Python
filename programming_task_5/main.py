from order import Orders
from validation1 import validate_file_input


ls = Orders()
file_name = validate_file_input()
ls.fill_list_from_file(file_name)
while True:
    userchoice = input('''welcome user choose your choice:
    1.) Search orders with value
    2.) Delete orders by ID
    3.) Add order
    4.) Edit order by ID
    5.) Print all orders
    6.)Exit''' + '\n')
    if userchoice == '1':
        val = input('Input value for order: ')
        ls.search_in_list(val)

    elif userchoice == '2':
        id = int(input('Input id: '))
        ls.remove(file_name, id)
    elif userchoice == '3':
        new_order = input('Input info for new order: ')
        ls.add(new_order, file_name)
    elif userchoice == '4':
        id = input('Input id: ')
        new_order = input('Input info for new order: ')
        ls.edit(new_order, file_name, id)
    elif userchoice == '5':
        if type(ls) == 'NoneType':
            print('Your list_orders does not have any orders!')
        else:
            ls.print_list()
    elif userchoice == '6':
        print("thank fot using us !!!")
        break
    else:
        print('Wrong number of choice')