def capitalise_first(arr):
    result = []
    if len(arr) == 0:
        return result
    else:
        result.append(arr[0][0].upper() + arr[0][1:])
        return result + capitalise_first(arr[1:])


test_list = ['joseph', 'caolan', 'freya']
print(capitalise_first(test_list))
