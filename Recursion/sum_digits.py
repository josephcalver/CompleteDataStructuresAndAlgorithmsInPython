def sum_digits(n):
    assert 0 <= n == int(n), 'N must be a positive integer'
    if n == 0:
        return 0
    return int(n % 10) + sum_digits(int(n / 10))


print(sum_digits(745))
