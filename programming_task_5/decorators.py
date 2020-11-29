import re
from datetime import datetime

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

class timeconflict(Exception):
    pass
class amountwrong(Exception):
    pass

def validate_id(func):
    def inner_method(self, val):
        try:
            if str(val).isdigit() is False:
                raise IdIsNotUnique
        except IdIsNotUnique:
            print('wrong id')
            return func(self, None)
        else:
            return func(self, val)

    return inner_method

def validate_amount(func):
    def inner_method(self, val):
        try:
            if str(val).isdigit() is False:
                raise amountwrong
        except amountwrong:
            print('amount not digit ')
            return func(self, None)
        else:
            return func(self, val)

    return inner_method



def validate_date(func):
    def inner_method(self, val):
        try:
            dt = datetime.strptime(val, "%d.%m.%Y")
        except:
            print('wrong date')
            return func(self, None)
        else:
            return func(self, val)

    return inner_method

def validate_customer_email(func):
    def inner_method(self, val):
        try:
            result = re.match(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', val)
            if result is None:
                raise Wrongemailaddress
        except Wrongemailaddress:
            print('wrong customer_email')
            return func(self, None)
        else:
            return func(self, val)

    return inner_method





def validate_order_status(func):
    def inner_method(self, val):
        try:
            values = ["paid", "refunded", "notpaid"]
            if val not in values:
                raise Wrongorderstatus
        except Wrongorderstatus:
            print('wrong order_status')
            return func(self, None)
        else:
            return func(self, val)

    return inner_method

def validate_discount(func):
    def inner_method(self, val):
        try:
            f = "%"
            if f not in val:
                raise discountnotfloat
        except discountnotfloat:
            print('discount is not float')
            return func(self, None)
        else:
            return func(self, val)

    return inner_method