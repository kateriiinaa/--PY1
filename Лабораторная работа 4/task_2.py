def delete(list_, index=None):
    if index is None:
        index = list_[-1]

    list_before_value_to_delete = list_[:index]
    list_after_value_to_delete = list_[index+1:]

    return list_before_value_to_delete + list_after_value_to_delete

print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
