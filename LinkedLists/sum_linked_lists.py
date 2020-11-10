from LinkedLists.linked_list import LinkedList


def sum_lists(list_a, list_b):
    n1 = list_a.head
    n2 = list_b.head
    carry = 0
    result_list = LinkedList()

    while n1 or n2 or carry is not 0:
        result = carry
        carry = 0
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        result_list.add(int(result % 10))
        carry = int(result / 10)
    return result_list


list1 = LinkedList()
list1.add(7)
list1.add(1)
list1.add(6)

list2 = LinkedList()
list2.add(5)
list2.add(9)
list2.add(2)

list1.traverse()
list2.traverse()
print(sum_lists(list1, list2))

print("*" * 25)

list1 = LinkedList()
list1.add(4)
list1.add(7)
list1.add(9)

list2 = LinkedList()
list2.add(6)
list2.add(5)
list2.add(8)

list1.traverse()
list2.traverse()
print(sum_lists(list1, list2))