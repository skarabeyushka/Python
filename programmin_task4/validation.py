import Orderinfo
from os import path
import datetime
import re
class Wrongorderstatus(Exception):
    pass

class FileNotExist(Exception):
    pass
class Wrongemailaddress(Exception):
    pass

class Invaliddate(Exception):
    pass

class IdIsNotUnique(Exception):
    pass
class discountnotfloat(Exception):
    pass

class FieldNotExist(Exception):
    pass


def file_exist(file_name):
    if not path.exists(file_name):
        raise FileNotExist


def field_exist(element):
    if element not in Orderinfo.series:
        raise FieldNotExist
    return True


def is_integer(element):
    for char in element:
        if char < '0' or char > '9':
            raise TypeError

def is_float(dis):
    f="%"
    if f not in dis:
        raise discountnotfloat




def unique_id(my_id, my_list):
    for element in my_list:
        if element['_id'] == my_id:
            raise IdIsNotUnique

def order_status(status):
    values=["paid", "refunded", "notpaid"]
    if status not in values:
        raise Wrongorderstatus


def field_check(field_name, data):
    if field_exist(field_name):
        if field_name in ['_id', 'amount']:
            is_integer(data)
        elif field_name in ['discount']:
            is_float(data)
        elif field_name in ['order_date','shipped_date']:
            orderdate(data)
        elif field_name in ['customer_email']:
            checkemailaddres(data)
        elif field_name in ['order_status']:
            order_status(data)

def orderdate(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise Invaliddate


def checkemailaddres(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        return True
    else:
        raise Wrongemailaddress




def general_validate_address_data(line, order):
    split_line = line.split(';')
    is_integer(split_line[0])
    order_status(split_line[1])
    is_integer(split_line[2])
    is_float(split_line[3])
    orderdate(split_line[4])
    orderdate(split_line[5])
    checkemailaddres(split_line[6])
    unique_id(int(split_line[0]), order)
    return split_line

