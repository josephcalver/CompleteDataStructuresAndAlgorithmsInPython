from array import array

#   1. Create an array and traverse
print("#1:")

my_array = array('i', [1, 2, 3, 4, 5])
print(my_array)

for i in my_array:
    print(i)

#   2. Access individual element via index
print("#2:")

print(my_array[0])

#   3. Append a value to the array
print("#3:")

my_array.append(6)
print(my_array)

#   4. Insert value at specified index
print("#4:")

my_array.insert(0, 0)
print(my_array)

#   5. Extend array
print("#5:")

array_extension = array('i', [7, 8, 9])
my_array.extend(array_extension)
print(my_array)

#   6. Append items from list
print("#6:")

my_list = [10, 11, 12]
my_array.fromlist(my_list)
print(my_array)

#   7. Remove item
print("#7:")

my_array.remove(12)
print(my_array)

#   8. Remove last item with pop()
print("#8:")

my_array.pop()
print(my_array)

#   9. Find any item by index
print("#9:")

print(my_array[7])

#   10. Reverse array
print("#10:")

my_array.reverse()
print(my_array)
my_array.reverse()

#   11. Access array buffer info
print("#11:")

print(my_array.buffer_info())

#  12. Count occurrences of item
print("#12:")
my_array.append(9)
print(my_array)
print(my_array.count(9))

#  13. Convert array to string
print("#13:")
str_temp = my_array.tostring()
print(str_temp)
ints = array('i')
ints.fromstring(str_temp)
print(ints)

#  14. Convert array to list
print("#14:")

list_temp = my_array.tolist()
print(type(my_array))
print(type(list_temp))

#   15. Slice elements of array (end index not inclusive)

array_slice = my_array[3:7]
print(array_slice)
print(my_array[6:10])
print(my_array[7:])
print(my_array[:4])
print(my_array)