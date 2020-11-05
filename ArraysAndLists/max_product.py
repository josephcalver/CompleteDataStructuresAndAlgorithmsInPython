import numpy as np


def max_product(arr):
    assert arr is not None, "Input must not be empty array"
    max_prod = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] * arr[j] > max_prod:
                print("{} * {}".format(arr[i], arr[j]))
                max_prod = arr[i] * arr[j]
    return max_prod


test_array = np.array([1, 6, 5, 3, 7, 8, 90, 3, 5, 7, 8, 9, 10, 11])
print(max_product(test_array))
