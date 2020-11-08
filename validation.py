import os


class StrategyisWrong(Exception):
    pass


class OptionisWrong(Exception):
    pass


class PositionisWrong(Exception):
    pass


class PositionisError(Exception):
    pass


class QuantityisWrong(Exception):
    pass


class WrongDataFile(Exception):
    pass


class WrongKinput(Exception):
    pass


def validate_file_input():
    while True:
        file = input('Input name of your file: ')
        try:
            if not os.path.isfile(file):
                raise FileExistsError
            else:
                f = open(file, 'r')
                ls = [i for i in ''.join(f.readlines()).split()]
                f.close()
                for i in ls:
                    if i.isalpha() is True:
                        raise WrongDataFile
        except FileExistsError:
            print('File not exists, try again')
        except WrongDataFile:
            print('Some elements are not numbers in file')
            return
        else:
            return file


def validate_input(parameter,value=None,order=None):
    while True:
        try:
            n = int(input('Input ' + parameter + ': '))
            if parameter == 'strategy':
                if n not in [1, 2]:
                    raise StrategyisWrong
            elif parameter == 'option':
                if n <= 0 or n >= 9:
                    raise OptionisWrong
            elif parameter == 'position to insert' or parameter == 'start_pos' or parameter == 'end_pos':
                if n <= 0:
                    raise PositionisWrong
                elif n > value + 1 and order is None:
                    raise PositionisWrong
                elif n > value and order == 'delete':
                    raise PositionisError
            elif parameter == 'quantity of elements':
                if n <= 0:
                    raise QuantityisWrong
            elif parameter == 'k':
                if n < 1:
                    raise WrongKinput
        except ValueError:
            print(parameter, 'should be a number please fix the value entered')
        except StrategyisWrong:
            print('Strategy can be equal 1 or 2 not another value please fix the value entered')
        except OptionisWrong:
            print('Please enter value available from the list above maximum is 8 ')
        except PositionisWrong:
            print('Position have to be more than 1  not less please fix the value entered')
        except PositionisError:
            print('List has only', str(value), 'elements')
        except QuantityisWrong:
            print('Quantity have to  be ')
        except WrongKinput:
            print('k should be more than 1 not less please fix the value entered ')
        else:
            return n