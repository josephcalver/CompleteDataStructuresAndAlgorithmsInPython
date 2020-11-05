import numpy as np

two_dimensional_array = np.array([[11, 15, 10, 6],
                                  [10, 14, 11, 5],
                                  [12, 17, 12, 8],
                                  [15, 18, 14, 9]
                                  ])
print(two_dimensional_array)
print()

new_two_dimensional_array = np.insert(two_dimensional_array, 1, [1, 2, 3, 4], axis=0)
print(new_two_dimensional_array)
print()

new_two_dimensional_array = np.append(two_dimensional_array, [[5, 6, 7, 8]], axis=0)
print(new_two_dimensional_array)


def traverse_two_dimensional_array(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j])


traverse_two_dimensional_array(two_dimensional_array)
print()


def search_two_dimensional_array(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is present at index: ' + str(i) + ", " + str(j)
    return 'The value is not present'


print(search_two_dimensional_array(two_dimensional_array, 17))
print()

another_two_dimensional_array = np.delete(new_two_dimensional_array, 0, axis=0)
print(another_two_dimensional_array)

string_array = np.array(['Joseph', 'Caolan', "Freya"])
print(string_array)
print()

print(14 in two_dimensional_array)
print(two_dimensional_array[-1][-1])

my_list = [1, 3, 2, 4, 6, 5]
sorted_list = sorted(my_list)
print(sorted_list)
print(my_list)