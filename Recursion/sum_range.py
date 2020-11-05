def sum_range(num):
    assert int(num) == num and num >= 0, 'Input must be a positive integer'
    if num == 0:
        return 0
    else:
        return num + sum_range(num - 1)


print(sum_range(7))
