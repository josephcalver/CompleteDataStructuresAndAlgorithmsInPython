import numpy as np


def recursive_with_callback(arr, cb):
    if len(arr) == 0:
        return False
    if cb(arr[0]):
        return True
    else:
        return recursive_with_callback(arr[1:], cb)


def is_odd(int):
    if int % 2 == 0:
        return False
    else:
        return True


arr = np.array([2, 1, 2, 4])
print(recursive_with_callback(arr, is_odd))
