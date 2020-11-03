def factorial(n):
    # assert n >= 0 and int(n) == n, 'N must be a positive integer'
    assert 0 <= n == int(n), 'N must be a positive integer'
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)


answer = factorial(4)
print(answer)
