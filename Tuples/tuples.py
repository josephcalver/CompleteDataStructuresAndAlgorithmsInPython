first_tuple = ('a', 'b', 'c', 'd', 'e')
second_tuple = tuple('abcde')
print(first_tuple)
print(second_tuple)
print(first_tuple[1])
print(first_tuple[-1])
print(first_tuple[:1])

for i in first_tuple:
    print(i)

for i in range(len(second_tuple)):
    print(second_tuple[i])

for index, value in enumerate(second_tuple):
    print(index, value)

print('f' in first_tuple)


def search_tuple(tup, val):
    for item in tup:
        if item == val:
            return "Value exists at index {}".format(tup.index(val))
    return "Item does not exist in tuple"


print(search_tuple(first_tuple, 'f'))

combined_tuple = first_tuple + second_tuple
print(combined_tuple)
multiplied_tuple = first_tuple * 4
print(multiplied_tuple)
print('d' in multiplied_tuple)
print(multiplied_tuple.count('c'))  # occurences of value, NOT # elements as in Java
print(len(multiplied_tuple))        # elements
print(max(multiplied_tuple))
tuple_from_list = tuple([1, 2, 3, 4, 5])
print(tuple_from_list)
