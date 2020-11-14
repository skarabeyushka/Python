from tackiclass2 import Takci
import validation

def main():
    cont = 'y'
    while cont == 'y':
        try:
            file_name = input("Enter file name: ")
            validation.validate_file_exist(file_name)
            break
        except validation.FileNotExist:
            print("You have entered an incorrect file name")
            cont = input("type y if you want to continue running the program ")
    if cont != 'y':
        return

    takci = Takci()
    takci.input(file_name)

    while True:
        try:
            userchoice = int(input('Choose what you want to do\n'
                                   '1 - print list of takci\n'
                                   '2 - add takci\n'

                                   ))

            if userchoice == 1:
                print("the list is :")


            elif userchoice == 2:
                takci.append(input('Enter new record with ; as a separator in these order  (_id;order_status;'
                                   'amount;discount;order_date;shipped_date;customer_email) '))
                takci.newinput_file(file_name)

        except Exception:
            print("oops , Something went wrong")
        if input("press y if you want to continue running the program ") != 'y':
            break


if __name__ == '__main__':
    main()