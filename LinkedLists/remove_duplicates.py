from LinkedLists.linked_list import LinkedList


def remove_duplicates(linked_list):
    if linked_list.head is None:
        print("List is empty")
        return

    node = linked_list.head
    checked = {node.value}      # set
    # print(checked)
    while node.next:
        # print(node.next)
        if node.next.value in checked:
            # print("Removing: {}".format(node.next))
            node.next = node.next.next
            # print("New next = {}".format(node.next))
        else:
            checked.add(node.next.value)
            node = node.next
        print(checked)


def remove_duplicates_no_buffer(linked_list):
    if linked_list.head is None:
        print("List is empty")
        return

    current_node = linked_list.head
    while current_node:
        runner = current_node
        while runner.next:
            if current_node.value == runner.next.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current_node = current_node.next


llist = LinkedList()
llist.add(1)
llist.add(2)
llist.add(3)
llist.add(4)
llist.add(3)
llist.add(2)
llist.add(2)
llist.add(5)
llist.add(1)

llist.traverse()
remove_duplicates(llist)
llist.traverse()

print("*" * 10)

llist2 = LinkedList()
llist2.generate(10, 0, 20)
llist2.traverse()
remove_duplicates_no_buffer(llist2)
llist2.traverse()
