import sys
import random

#Covers contens of Chapt 1, 1.1.1 pages 2 - 3
#Purpose here to define fundamental concepts (greater than, addition, etc) in definition/conditions used in book

#length is here used as means to illustrate attribution of quantities to qualitative observations
#transitive property
def is_greater(a, b):
    if a > b:
        return True
    return False

#"We require a > b only if the function of a is grea   ter than the functino of b
#In transitve property in this case, a and be are results of functions
#Ordinal relationships fullfilable by all numeric cases, except where a ~ b
def is_equivalent(a, b):
    if not a > b and not a < b:
        return True
    return False

#We assign to first rod any number, a larger rod a larger number, a smaller rod a smaller, etc.
#In event a ~ b.Procedure for ordinal measuremnt is only suitable in the event precision yields allows for it


if __name__== "__main__":
    a_values = random.sample(range(0, sys.maxsize), 1000)
    b_values = random.sample(range(0, sys.maxsize), 1000)
    ord_dict = {'a': a_values, 'b': b_values}
    for value_index in range(len(ord_dict['a'])):
        a = ord_dict['a'][value_index]
        b = ord_dict['b'][value_index]
        output_tuple = (a, b)
        try:
            if is_greater(a, b):
                result = 1
                print('a with value %s is greater than b with value %s' % output_tuple)
            elif is_greater(b, a):
                result = 2
                print('a with value %s is less than b with value %s' % output_tuple)
            elif is_equivalent(a, b):
                result = 3
                print('a with value %s is equal to b with value %s' % output_tuple)
            else:
                result = 666
            assert result != 666
        except AssertionError:
            print('The foundations of science are a lie and humanity is doomed. DOOOOOMMMMMED')
            raise








