from pprint import pprint

amount_ = 15
dict_comprehension = [{'bin': bin(num_), 'dec': num_, 'hex': hex(num_), 'oct': oct(num_)}
                      for num_ in range(amount_ + 1)]

pprint(dict_comprehension)
# Перенос строки