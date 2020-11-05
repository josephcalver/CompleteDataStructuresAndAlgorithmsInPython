import numpy as np


def find_num(arr, num):
    assert arr is not None and int(num) == num, 'Search param must be an integer'
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return "None found"


test_array = np.array([6, 23, 8, 6, 3, 7, 0, 29, 8])
print(find_num(test_array, 28))
