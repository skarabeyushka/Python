from validation import validate_input,validate_file_input
from linked_list import LinkedList
from abstract_class import Abstract_Class

if __name__ == '__main__':
    linked_list = LinkedList()
    abstract_class1 = Abstract_Class(1)
    while True:
        print(''' Welcome User !!!!!!! 
          choose your option :
          1-) Usage of first strategy 
          2-) Usage of second strategy
          3-) Data entering
          4-) Remove element of list by position 
          5-) Remove elements of list by range
          6-) Count prime numbers exist in the list
          7-) Print list
          8-) Exit
        ''')
        userchoice = validate_input('option')
        if userchoice == 1:
            abstract_class1.choose_strategy(1)
        elif userchoice == 2:
            abstract_class1.choose_strategy(2)
        elif userchoice == 3:
         if abstract_class1.return_strategy_number() == 1:
            n = validate_input('number of elements')
            a = validate_input('left_border', linked_list.length_of_linked_list())
            b = validate_input('right_border', linked_list.length_of_linked_list())
            pos = validate_input('position to insert', linked_list.length_of_linked_list())
            linked_list = abstract_class1.do(linked_list, n, a, b, pos)
         elif abstract_class1.return_strategy_number() == 2:
            pos = validate_input('position to insert', linked_list.length_of_linked_list())
            file_name = validate_file_input()
            linked_list = abstract_class1.do(linked_list, pos, file_name)
        elif userchoice == 4:
            position = validate_input('position to insert', linked_list.length_of_linked_list(), 'delete')
            linked_list.pop_node(position)
        elif userchoice == 5:
            position1 = validate_input('start_position', linked_list.length_of_linked_list())
            position2 = validate_input('end_position', linked_list.length_of_linked_list())
            linked_list.pop_nodes_in_range_mode(position1, position2)
        elif userchoice == 6:
            num = linked_list.countPrime()
            print("count of prime numbers exist is ",num)
        elif userchoice == 7:
            print(linked_list)
        elif userchoice == 8:
            print("have a great day !!!")
            break