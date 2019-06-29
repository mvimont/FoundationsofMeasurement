from Chapter1.ThreeProceduresBasicMeasurement.Ordinal.OrdinalClass import Ordinal

class Counting(Ordinal):
    def __init__(self):
        super().__init__()

    def concatenation(self, a, b):
        return a + b

    def copy(self, a):
        return a

    def standard_sequence(self, a, number):
        sequence = []
        sum = 0
        for duplicate in range(number):
            sum = sum + self.copy(a)
            sequence.append(sum)
        return sequence

    def is_ordinal(self, seq_list):
        for item in seq_list:
            loc = seq_list.index(item)
            if seq_list.count(item) > 1:
                return False
            if self.is_equivalent(loc, 0):
                continue
            if self.is_equivalent(loc, seq_list.index(seq_list[-1])):
                return True
            if self.is_greater(item, seq_list[loc - 1]) and self.is_greater(seq_list[loc + 1], item):
                continue
            else:
                return False

    def is_ratio(self, seq_list):
        base_unit = seq_list[0]
        for item in seq_list:
            if self.is_equivalent(item % base_unit, 0):
                continue
            else:
                return False
        return True

    def valid_standard_seq_counting(self, seq_list):
        if self.is_ratio(seq_list) and self.is_ordinal(seq_list):
            return True
        return False

if __name__=="__main__":
    c = Counting()
    l = c.standard_sequence(2, 100)
    print(l)
    if c.valid_standard_seq_counting(l):
        print('Valid counting procedure using standard sequence')
    else:
        print('Invalid counting procedure using standard sequence')