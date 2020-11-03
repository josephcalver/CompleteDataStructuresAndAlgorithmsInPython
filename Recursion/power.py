def power(base, exp):
    assert 0 <= exp == int(exp), 'Exponent must be a positive integer'
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base, exp - 1)


print(power(2, 4))
