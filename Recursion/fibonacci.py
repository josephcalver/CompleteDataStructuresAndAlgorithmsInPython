def fibonacci(n):
    assert 0 <= n == int(n), 'N must be a positive integer'
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))
