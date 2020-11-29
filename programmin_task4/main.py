from orderclass import Order
import validation

def main():
    cont = 'y'
    while cont == 'y':
        try:
            file_name = input("Enter file name: ")
            validation.file_exist(file_name)
            break
        except validation.FileNotExist:
            print("You have entered an incorrect file name")
            cont = input("type y if you want to continue running the program ")
    if cont != 'y':
        return

    order = Order()
    order.input(file_name)

    while True:
        try:
            userchoice = int(input('Choose what you want to do\n'
                               '1 - sort orders\n'
                               '2 - search orders\n'
                               '3 - delete orders\n'
                               '4 - add orders\n'
                               '5 - edit orders\n'))

            if userchoice == 1:

                input_choice = input('Which column do you want to sort(_id;order_status;'
                                    'amount;discount;order_date;shipped_date;customer_email)? ')
                order.sort_by(input_choice)
                print(order)
            elif userchoice == 2:

                search_request = input('Enter your search request: ')
                result = order.search(search_request)
                print('the results are : ')
                for element in result:
                    print(element)
            elif userchoice == 3:

                order.del_element_at(int(input('Enter index for delete element: ')) - 1)
                order.newinput_file(file_name)
            elif userchoice == 4:

                order.append(input('Enter new record with ; separator (_id;order_status;'
                                    'amount;discount;order_date;shipped_date;customer_email)? '))
                order.newinput_file(file_name)
            elif userchoice == 5:

                theindex = int(input('Enter index of your record: ')) - 1
                theseries = input('Enter name of series: ')
                newvalue = input('Enter new value for it: ')
                order.edit_record(theindex, theseries, newvalue)
                order.newinput_file(file_name)

        except Exception:
            print("oops , Something went wrong")
        if input("press y if you want to continue running the program ") != 'y':
            break


if __name__ == '__main__':
    main()