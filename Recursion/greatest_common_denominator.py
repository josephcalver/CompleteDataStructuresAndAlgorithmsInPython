def gcd(a, b):
    assert int(a) == a and int(b) == b, 'a and b must be integers'
    if a < 0:
        a = abs(a)
    if b < 0:
        b = abs(b)

    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(-48, -18))
