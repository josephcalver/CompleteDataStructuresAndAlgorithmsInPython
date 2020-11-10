from LinkedLists.linked_list import LinkedList


def find_kth_from_last(llist, k):
    leader = llist.head
    kth_node = llist.head

    for i in range(k):
        if leader is None:
            return None
        else:
            leader = leader.next

    while leader:
        leader = leader.next
        kth_node = kth_node.next

    return kth_node


singly_llist = LinkedList()
singly_llist.generate(10, 0, 99)
singly_llist.traverse()
print(find_kth_from_last(singly_llist, 3))
