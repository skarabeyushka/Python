from order_class import OnlineOrder
from datetime import datetime as dt
class Orders:
    unique_ind = []

    def __init__(self):
        self.orders = []

    def add_to_list(self, order: OnlineOrder):
        self.orders.append(order)

    def remove_from_list(self, id):
        for i in range(len(self.orders)):
            if self.orders[i].get_field('id') == int(id):
                del self.orders[i]
                return


    def change(self, ind, order: OnlineOrder):
        self.orders[ind] = order

    def __getitem__(self, item):
        return self.orders[item]

    def print_list(self):
        for i in range(0, len(self.orders)):
            print(self.orders[i])

    def search_in_list(self, value):
        for i in self.orders:
            if i.search(value):
                print(i)

    def compare(self, param, x, y):
        if param == 'order_date':
            a = dt.strptime(x, "%d.%m.%Y")
            b = dt.strptime(y, "%d.%m.%Y")
            if a > b:
                return True
        return False

    def sort(self, param):
        for i in range(len(self.orders)):
            for j in range(len(self.orders) - i - 1):
                a = self.orders[j].get_field(param)
                b = self.orders[j + 1].get_field(param)
                if self.compare(param, a, b):
                    self.orders[j], self.orders[j + 1] = self.orders[j + 1], self.orders[j]

    def rewrite_file(self, file):
        with open(file, 'w') as f:
            for i, elem in enumerate(self.orders):
                if i != len(self.orders) - 1:
                    f.write(elem.str_format() + '\n')
                else:
                    f.write(elem.str_format())
        f.close()

    def add(self, val, file, param=None):
        arg = val.split()
        if len(arg) != 7:
            print('Not all arguments were inputeddd')
            return
        obj = OnlineOrder(arg)
        if obj.exist():
            if self.unique_ind.count(arg[0]) == 0:
                self.add_to_list(obj)
                self.unique_ind.append(arg[0])
                if param is None:
                    self.rewrite_file(file)
            else:
                print('Id is not unique')

    def del_element_at(self, id):
        self.orders.pop(id)

    def remove(self, file, id):
        self.del_element_at(id)
        self.rewrite_file(file)



