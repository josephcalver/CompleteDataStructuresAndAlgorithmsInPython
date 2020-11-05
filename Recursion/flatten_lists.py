def flatten(lst):
    result_array = []
    for item in lst:
        if type(item) is list:
            result_array.extend(flatten(item))
        else:
            result_array.append(item)
    return result_array


test_list = [1, 2, [3, 4, 5, [6, 7, [8, 9, 10]]]]
print(flatten(test_list))
