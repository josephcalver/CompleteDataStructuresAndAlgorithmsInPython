def capitalise_words(lst):
    result = []
    if len(lst) == 0:
        return result
    else:
        result.append(lst[0].upper())
        return result + capitalise_words(lst[1:])


test_list = ['joseph', 'caolan', 'freya']
print(capitalise_words(test_list))
