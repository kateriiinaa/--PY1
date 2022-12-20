import json

INPUT_FILE = "input2.csv"


def csv_to_list_dict(filename='', delimiter=None, new_line=None) -> list[dict]:
    if delimiter is None:
        delimiter = ','
    if new_line is None:
        new_line = '\n'

    new_list = []
    with open(filename) as f:
        for first_line in f:
            first_list_line = list((first_line.rstrip()).split(','))
            for other_line in f:
                other_list_line = list((other_line.rstrip()).split(','))
                dict_ = {first_list_line[i]: other_list_line[i] for i in range(len(first_list_line))}
                new_list.append(dict_)
    return new_list

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
#Перенос строки