import random
import math
import sys

#length is here used as means to illustrate attribution of quantities to qualitative observations

#transitive property
def is_transitive(a, b):
    if a > b:
        return True
    return False

#associative property
def is_associative(a, b, c):
    if a > b and c > b or a < b and c < b:
        return True
    return False

#"We require a > b only if the function of a is greater than the functino of b
def is_transitive_function(phia, phib):
    if is_transitive(phia(), phib()):
        return True
    return False

#We assign to first rod any number, a larger rod a larger number, a smaller rod a smaller, etc.
#In even a ~ b.Procedure for ordinal measuremnt is only suitable in the event precision yields allows for it
#Coder's note: exception provieds for equality

def basic_ordinal():
    #a = random.uniform(0, math.inf)
    a = random.uniform(0, sys.maxsize)
    b = random.uniform(a, sys.maxsize)
    c = random.uniform(0, a)
    return sorted([a, b, c])


print(basic_ordinal())






