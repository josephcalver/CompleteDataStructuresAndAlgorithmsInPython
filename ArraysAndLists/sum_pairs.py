# find consecutive integers that sum to given number
def sum_pairs(lst, num):
    for i in range(len(lst) - 1):
        if lst[i] + lst[i+1] == num:
            print("Found Pair: {} + {} = {}".format(lst[i], lst[i+1], num))


# find any combination of integers in the array that sum to given number
def sum_pairs_nested(lst, num):
    print(len(lst))
    for i in range(len(lst)-1):
        print("i = {}".format(i))
        for j in range(i+1, len(lst)):
            print("j = {}".format(j))
            if lst[i] + lst[j] == num:
                print("Found Pair: {} + {} = {}".format(lst[i], lst[i+1], num))



test_list = [6, 3, 2, 9, 7, 1, 11, 4]
sum_pairs(test_list, 5)
print()
sum_pairs_nested(test_list, 5)

