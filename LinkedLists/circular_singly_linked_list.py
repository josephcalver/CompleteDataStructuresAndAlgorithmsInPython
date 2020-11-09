class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def insert(self, value, index):
        new_node = Node(value)
        # list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = new_node
        else:
            # insert node at beginning
            if index == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            # insert node at end
            elif index == -1:
                new_node.next = self.tail.next
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                i = 0
                while i < index - 1:
                    temp_node = temp_node.next
                    i += 1
                print("index = {}".format(index))
                print("temp node value = {}".format(temp_node.value))
                print("new node value = {}".format(new_node.value))
                new_node.next = temp_node.next
                temp_node.next = new_node

    def delete(self, index):
        if self.head is None:
            print("List is empty")
        else:
            # delete from beginning
            if index == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif index == -1:
                penultimate = self.head
                while penultimate.next != self.tail:
                    penultimate = penultimate.next
                penultimate.next = self.head
                self.tail = penultimate
            else:
                previous = self.head
                i = 0
                while i < index - 1:
                    previous = previous.next
                    i += 1
                previous.next = previous.next.next

    def delete_list(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = None
            self.tail = None
            print("List deleted")

    def traverse(self):
        if self.head is None:
            print("List is empty")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    break

    def find(self, value):
        if self.head is None:
            print("List is empty")
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == value:
                    print("Value exists in list")
                    break
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    print("Value not found in list")
                    break


circular_singly_linked_list = CircularSinglyLinkedList()
circular_singly_linked_list.insert(1, 0)
circular_singly_linked_list.insert(2, 0)
circular_singly_linked_list.insert(3, 0)
circular_singly_linked_list.insert(4, 0)
print([node.value for node in circular_singly_linked_list])
circular_singly_linked_list.traverse()
circular_singly_linked_list.find(5)
print("*" * 10)
print([node.value for node in circular_singly_linked_list])
circular_singly_linked_list.delete(2)
print([node.value for node in circular_singly_linked_list])
circular_singly_linked_list.delete(1)
print([node.value for node in circular_singly_linked_list])
