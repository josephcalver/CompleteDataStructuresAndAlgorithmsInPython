class Node:

    def __init__(self, value=None):
        self.value = value
        self.previous = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value, index):
        new_node = Node(value)
        # if list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # insert at beginning
            if index == 0:
                # new_node.previous defaults to None
                new_node.next = self.head
                self.head.previous = new_node
                self.head = new_node
            # insert at end
            elif index == -1:
                new_node.previous = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                previous = self.head
                i = 0
                while i < index - 1:
                    print("{}".format(previous.value))
                    previous = previous.next
                    i += 1
                new_node.previous = previous
                new_node.next = previous.next
                new_node.next.previous = new_node
                previous.next = new_node

    def delete(self, index):
        if self.head is None:
            print("List is empty")
        else:
            # delete from beginning
            if index == 0:
                # if only one node in list
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.previous = None
            # delete from end
            elif index == -1:
                # if only one node in list
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.previous
                    self.tail.next = None
            # delete from index
            else:
                previous_node = self.head
                i = 0
                while i < index - 1:
                    previous_node = previous_node.next
                    i += 1
                previous_node.next = previous_node.next.next
                previous_node.next.previous = previous_node

    def traverse(self):
        if self.head is None:
            print("List is empty")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next

    def reverse_traversal(self):
        if self.tail is None:
            print("List is empty")
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.previous

    def find(self, value):
        if self.head is None:
            print("List is empty")
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == value:
                    print("Value {} exists in list".format(temp_node.value))
                    break
                temp_node = temp_node.next
            else:
                print("Value {} not found in list".format(value))


doubly_linked_list = DoublyLinkedList()
doubly_linked_list.insert(5, 0)
doubly_linked_list.insert(10, 0)
doubly_linked_list.insert(0, -1)
doubly_linked_list.insert(20, 1)
doubly_linked_list.insert(25, 2)
print([node.value for node in doubly_linked_list])
doubly_linked_list.traverse()
print("*" * 10)
doubly_linked_list.reverse_traversal()
doubly_linked_list.find(25)
print([node.value for node in doubly_linked_list])
doubly_linked_list.delete(3)
print([node.value for node in doubly_linked_list])
doubly_linked_list.delete(0)
print([node.value for node in doubly_linked_list])
doubly_linked_list.delete(-1)
print([node.value for node in doubly_linked_list])
