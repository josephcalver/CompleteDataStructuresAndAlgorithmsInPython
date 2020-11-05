def permutation(first_word, second_word):
    assert str(first_word) == first_word and \
           str(second_word) == second_word, 'Parameter(s) cannot be null'

    # if str(first_word).count() != str(second_word).count():
    if len(first_word) != len(second_word):
        print("Words do not have the same number of characters")
        return False

    first_chars = list(first_word)
    second_chars = list(second_word)

    first_chars.sort()
    second_chars.sort()
    print(first_chars)
    print(second_chars)

    for i in range(len(first_chars)):
        if first_chars[i] != second_chars[i]:
            return False
    return True


first_word = 'coffee'
second_word = 'feefoc'
print(permutation(first_word, second_word))
