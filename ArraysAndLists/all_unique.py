def all_unique(lst):
    checked = []
    for i in lst:
        if i in checked:
            print(i)
            return False
        else:
            checked.append(i)
    return True


test_list = [1, 1, 2, 3, 4, 5]
print(all_unique(test_list))
