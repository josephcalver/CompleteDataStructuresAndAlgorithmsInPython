english_to_spanish = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(english_to_spanish['two'])
# print(english_to_spanish['four'])
print()
for key in english_to_spanish:
    print(key, english_to_spanish[key])

print()
for index, key in enumerate(english_to_spanish):
    print(index, key, english_to_spanish[key])
print()


def search_dictionary(dict, key):
    if key in dict:
        print(dict[key])


search_dictionary(english_to_spanish, 'two')
print()

backup = english_to_spanish.copy()
print("Backup: {}".format(backup))

backup.clear()
print("Backup: {}".format(backup))

del english_to_spanish['three']
print(english_to_spanish)
english_to_spanish.pop('two')
print(english_to_spanish)
english_to_spanish.popitem()
print(english_to_spanish)

new_dictionary = {}.fromkeys([1, 2, 3], 0)
print(new_dictionary)
print(new_dictionary.get(4))
print(new_dictionary.items())
print(new_dictionary.keys())
print(new_dictionary.values())
another_dictionary = {'a': '1', 'b': '2', 'c': '3'}
new_dictionary.update(another_dictionary)   # similar to extend with lists -- adds or updates
print(new_dictionary)
updated_dictionary = {'a': '4', 'b': '5', 'c': '6'}
new_dictionary.update(updated_dictionary)
print(new_dictionary)
print('6' in new_dictionary.values())

char_dictionary = {'a': '1', 'd': '4', 'c': '3', 'b': '2'}
print(sorted(char_dictionary, reverse=True))
