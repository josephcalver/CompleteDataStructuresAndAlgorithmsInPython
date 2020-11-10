from LinkedLists.linked_list import LinkedList


def partition(linked_list, x):
    if linked_list.head is None:
        print("List is empty")

    current_node = linked_list.head
    linked_list.tail = linked_list.head

    while current_node:
        next_node = current_node.next
        current_node.next = None
        if current_node.value < x:
            current_node.next = linked_list.head
            linked_list.head = current_node
        else:
            linked_list.tail.next = current_node
            linked_list.tail = current_node
        current_node = next_node

    # if linked_list.tail.next is not None:
    #     linked_list.tail.next = None


test_list = LinkedList()
test_list.generate(10, 0, 10)
test_list.traverse()
partition(test_list, 5)
test_list.traverse()
