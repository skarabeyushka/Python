import takciclass
from os import path
import datetime
class Wrongstr(Exception):
    pass

class Wrongtype(Exception):
    pass
class Wrongstarttime(Exception):
    pass
class Wrongendtime(Exception):
    pass
class FieldNotExist(Exception):
    pass
class FileNotExist(Exception):
    pass
class timeincorrectness(Exception):
    pass


def validate_file_exist(file_name):
   if not path.exists(file_name):
        raise FileNotExist

def validate_field_exist(element):
    if element not in takciclass.series:
        raise FieldNotExist
    return True

def is_str(n):
   k=isinstance(n,str)
   if (k != True):
       raise Wrongstr

def tacki_type(type):
    types=["econom", "standart", "confort", "minibus"]
    if type not in types:
        raise Wrongtype


def validation_field_exist(field_name, data):
    if validate_field_exist(field_name):
        if field_name in ['name', 'start_place','end_place']:
               is_str(data)
        elif field_name() in ['Type']:
            tacki_type(data)

def cameraspeedcheck(n):
    timeformat = "%H:%M"
    try:
        validtime = datetime.datetime.strptime(n, timeformat)

    except ValueError:
        raise Wrongstarttime


def validate_all(line,taxi):
    split_line = line.split(';')
    is_str(split_line[0])
    is_str(split_line[4])
    is_str(split_line[5])
    tacki_type(split_line[1])
    return split_line






