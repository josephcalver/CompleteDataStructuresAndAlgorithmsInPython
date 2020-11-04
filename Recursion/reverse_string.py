def reverse_string(string):
    print(string)
    assert str(string) == string and string is not None, 'Input must be a string'
    n = len(string)
    print("n = {}".format(n))
    if n == 1:
        return string[0]
    else:
        return string[n-1] + reverse_string(string[:n-1])


print(reverse_string("python"))
