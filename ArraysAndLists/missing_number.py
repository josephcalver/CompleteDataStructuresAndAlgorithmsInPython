def find_missing(lst):
    # sum of sequence = n(n+1) / 2
    # Item is missing from list, so use n+1 to compute what sum should be: len+1(len+2) / 2
    # Subtract the sum of the items we do have to find value of missing item
    return ((len(lst) + 1) * (len(lst) + 2) / 2) - sum(lst)


test_list = [1, 2, 4, 5]
print(find_missing(test_list))
