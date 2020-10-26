import validation
from takciclass import takciinfo

class Takci:

    def __init__(self):
        self.taxi = []

    def __getitem__(self, item):
        return self.taxi[item]
    def input(self, file_name):
        file = open(file_name, 'r')
        for line in file:
            self.append(line)
        file.close()

    def del_element_at(self, position):
        self.taxi.pop(position)

    def append(self,line):
        try:
            split_line = validation.validate_all(line,self.taxi)
        except validation.Wrongstr:
            print('The string "', line, '" was not imported because you didnt enter a stirng data type ')
            return
        except validation.Wrongtype:
            print('The string "', line, '" was not imported because worn type of takci was entered ')
        except validation.Wrongstarttime:
            print('The string "', line, '" was not imported because you didnt enter a correct time format ')
        except ValueError:
            print('the string"',line,'"was not imported ')
        self.taxi.append(takciinfo(*split_line))

    def __str__(self):
        result = ''
        for orders in self.taxi:
            result += str(orders)
        return result

    def newinput_file(self, file_name):
        file = open(file_name, 'w')
        for orders in self.taxi:
            file.write(orders.get_str())
        file.close()



