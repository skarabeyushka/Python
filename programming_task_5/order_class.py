from decorators import *
series = ['id', 'order_status', 'amount', 'discount', 'order_date', 'shipped_date', 'customer_email']




class OnlineOrder:

    def __init__(self, args):
        for i, elem in enumerate(args):
            if i < 7:
                setattr(self, series[i], elem)






    @property
    def id(self):
        return self._id

    @id.setter
    @validate_id
    def id(self, val):
        self._id = val
        if self._id is not None:
            self._id = int(self._id)

    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    @validate_order_status
    def order_status(self, val):
        self._order_status = val

    @property
    def amount(self):
        return self._amount

    @amount.setter
    @validate_amount
    def amount(self, val):
        self._amount = val


    @property
    def discount(self):
        return self._discount

    @discount.setter
    @validate_discount
    def discount(self, val):
        self._discount = val



    @property
    def order_date(self):
        return self._order_date

    @order_date.setter
    @validate_date
    def order_date(self, val):
        self._order_date = val

    @property
    def shipped_date(self):
        return self._shipped_date

    @shipped_date.setter
    @validate_date
    def shipped_date(self, val):
        self._shipped_date = val

    @property
    def customer_email(self):
        return self._customer_email

    @customer_email.setter
    @validate_customer_email
    def customer_email(self, val):
        self._customer_email = val






    def __repr__(self):
        d1 = self.__dict__
        s = ''
        for i in d1:
            s += i + ': ' + str(d1[i]) + '\n'
        return s

    def str_format(self):
        d1 = self.__dict__
        s = ''
        for i in d1:
            s += str(d1[i]) + ' '
        s = s.rstrip(' ')
        return s


    def compare(self, other):
        d1 = self.__dict__
        for param in d1.keys():
            if getattr(self, param) != getattr(other, param):
                return False
        return True

    def search(self, value):
        d1 = self.__dict__
        for i in d1.values():
            i = str(i)
            if value in i[0:len(i)]:
                return True

    def get_field(self, param):
        d1 = self.__dict__
        if param in d1.keys():
            return getattr(self, param)

    def exist(self):
        d1 = self.__dict__
        f = True
        for i in d1.values():
            if i is None:
                return False
        dt1 = datetime.strptime(self._order_date, "%d.%m.%Y")
        dt2 = datetime.strptime(self._shipped_date, "%d.%m.%Y")
        if dt1 > dt2:
            print('date conflict')
            f = False
        return f

    def change_field(self, param, value):
        if param in {'id', 'order_status', 'amount', 'discount', 'order_date', 'shipped_date', 'customer_email'}:
            setattr(self, param, value)