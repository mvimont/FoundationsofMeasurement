import sys
import random

class Ordinal:
    def __init__(self):
        a_list = []
        b_list = []

    def set_values(self, values_tuple=None):
        if not values_tuple:
            self.a_list = random.sample(range(0, sys.maxsize), 1000)
            self.b_list = random.sample(range(0, sys.maxsize), 1000)
        else:
            for a, b in values_tuple:
                self.a_list = a
                self.b_list = b

    def is_greater(self, a, b):
        if a and b and a > b:
            return True
        return False

    def is_equivalent(self, a, b):
        if not a > b and not a < b:
            return True
        return False

    def truth_test(self):
        self.set_values()
        for value_index in range(len(self.a_list)):
            a = self.a_list[value_index]
            b = self.b_list[value_index]
            output_tuple = (a, b)
            try:
                if self.is_greater(a, b):
                    result = 1
                    print('a with value %s is greater than b with value %s' % output_tuple)
                elif self.is_greater(b, a):
                    result = 2
                    print('a with value %s is less than b with value %s' % output_tuple)
                elif self.is_equivalent(a, b):
                    result = 3
                    print('a with value %s is equal to b with value %s' % output_tuple)
                else:
                    result = 666
                assert result != 666
            except AssertionError:
                print('The foundations of science are a lie and humanity is doomed. DOOOOOMMMMMED')
                raise

if __name__== "__main__":
    Ordinal().truth_test()


