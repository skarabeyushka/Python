import validation
from Orderinfo import orderinfo

class Order:

    def __init__(self):
        self.order = []

    def __getitem__(self, item):
        return self.order[item]

    def swap(self, ind1, ind2):
        self.order[ind1], self.order[ind2] = self.order[ind2], self.order[ind1]

    def search(self, element):
        result = []
        for orders in self.order:
            if orders.has_element(element):
                result.append(orders)
        return result

    def input(self, file_name):
        file = open(file_name, 'r')
        for line in file:
            self.append(line)
        file.close()

    def del_element_at(self, position):
        self.order.pop(position)

    def append(self,line):
        try:
            split_line = validation.general_validate_address_data(line,self.order)
        except validation.Wrongorderstatus:
            print('The string "', line, '" was not imported because wrong order status was entered')
            return
        except validation.IdIsNotUnique:
            print('The string "', line, '" was not imported because the Id is not  unique')
            return
        except validation.discountnotfloat:
            print('The string "', line, '" was not imported because discount is not float')
            return
        except validation.Invaliddate:
            print('The string "', line, '" was not imported because  order date was incorrect')
            return
        except validation.Invaliddate:
            print('The string "', line, '" was not imported because shipped date was incorrect')
            return
        except validation.Wrongemailaddress:
            print('The string "', line, '" was not imported because customers_email was incorrect')
            return
        except TypeError:
            print('The string "', line, '" was not imported because the wrong data type was entered')
            return
        except ValueError:
            print('the string"',line,'"was not imported ')
        self.order.append(orderinfo(*split_line))

    def __str__(self):
        result = ''
        for orders in self.order:
            result += str(orders)
        return result

    def newinput_file(self, file_name):
        file = open(file_name, 'w')
        for orders in self.order:
            file.write(orders.get_str_line_in_standard_form())
        file.close()

    def edit_record(self, ind, series, data):
        if series == 'id':
            validation.unique_id(data, self.order)
        self.order[int(ind)].put_element(series, data)

    def sort_by(self, series_for_sort):
        h = len(self.order) - 1
        l = 0
        stack = [0] * len(self.order)
        top = -1
        top += 1
        stack[top] = l
        top += 1
        stack[top] = h
        while top >= 0:
            h = stack[top]
            top -= 1
            l = stack[top]
            top -= 1

            p = self.partition(l, h, series_for_sort)

            if p - 1 > l:
                top += 1
                stack[top] = l
                top += 1
                stack[top] = p - 1

            if p + 1 < h:
                top += 1
                stack[top] = p + 1
                top += 1
                stack[top] = h

    def partition(self, l, h, series_for_sort):
        i = (l - 1)
        x = self[h][series_for_sort]
        if isinstance(x, str):
            x = x.lower()
            for j in range(l, h):
                if self[j][series_for_sort].lower() <= x:
                    i += 1
                    self.swap(i, j)
        else:
            for j in range(l, h):
                if self[j][series_for_sort] <= x:
                    i += 1
                    self.swap(i, j)
        self.swap(i + 1, h)
        return i + 1

