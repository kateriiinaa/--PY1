from random import randint

start = -10
stop = 10
count = 15

def get_unique_list_numbers() -> list[int]:
    list_numbers = set([randint(start, stop) for _ in range(count)])
    return list_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
# Перенос строки