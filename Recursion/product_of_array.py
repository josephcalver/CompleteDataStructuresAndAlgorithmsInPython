def product(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * product(arr[1:])


test_list = [1, 2, 3, 10]
print(product(test_list))
