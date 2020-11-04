def is_palindrome(string):
    assert str(string) == string and string is not None, 'Input must be a string'
    if len(string) == 1:
        return True
    if string[0] != string[len(string)-1]:
        return False
    else:
        return is_palindrome(string[1:len(string)-1])


print(is_palindrome("tacocat"))
