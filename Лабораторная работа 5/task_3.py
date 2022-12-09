from random import sample
import string

symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits

def get_random_password(n = None) -> str:
    if n is None:
        n = 8
    password = sample(symbols, n)

    return ("".join(password))

print(get_random_password())
# Перенос строки