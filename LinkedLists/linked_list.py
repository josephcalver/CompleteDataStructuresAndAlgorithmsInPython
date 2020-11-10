from random import randint


class Node:

    def __init__(self, value=None):
        self.value = value
        self.previous = None
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return " --> ".join(values)

    def __len__(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self

    def add(self, value):
        # add new node at end of list
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        return self.tail.value

    def insert(self, value, index):
        new_node = Node(value)
        # insert in empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # insert at beginning
            if index == 0:
                new_node.next = self.head
                self.head = new_node
            # insert at end
            elif index == -1:
                new_node.previous = self.tail
                self.tail.next = new_node
                self.tail = new_node
            # insert at index
            else:
                previous = self.head
                i = 0
                while i < index - 1:
                    previous = previous.next
                    i += 1
                new_node.next = previous.next
                previous.next.previous = new_node
                previous.next = new_node
                new_node.previous = previous

    def delete(self, index):
        # if list already empty
        if self.head is None:
            print("List is already empty")
        else:
            # only one node in list
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # delete from beginning
            elif index == 0:
                self.head = self.head.next
                self.head.previous = None
            # delete from end
            elif index == -1:
                previous = self.head
                i = 0
                while previous.next != self.tail:
                    previous = previous.next
                previous.next = None
                self.tail = previous
            # delete from index
            else:
                previous = self.head
                i = 0
                while i < index - 1:
                    previous = previous.next
                    i += 1
                previous.next = previous.next.next
                previous.next.previous = previous

    def traverse(self):
        if self.head is None:
            print("List is empty")
        else:
            cursor = self.head
            while cursor:
                print("{} --> ".format(cursor.value), end="")
                cursor = cursor.next
            else:
                print()

    def reverse_traverse(self):
        if self.head is None:
            print("List is empty")
        else:
            cursor = self.tail
            while cursor:
                print("{} --> ".format(cursor.value), end="")
                cursor = cursor.previous
            else:
                print()


if __name__ == '__Main__':
    linked_list = LinkedList()
    linked_list.insert(1, 0)
    linked_list.insert(2, -1)
    linked_list.insert(3, -1)
    linked_list.traverse()
    #linked_list.reverse_traverse()
    linked_list.insert(4, 2)
    linked_list.traverse()
    linked_list.delete(0)
    linked_list.traverse()
    linked_list.delete(-1)
    linked_list.traverse()
    #linked_list.delete(1)
    linked_list.traverse()
    linked_list.delete(0)
    linked_list.traverse()
    linked_list.add(8)
    linked_list.add(16)
    print(linked_list)
    print(linked_list.add(32))
    print(linked_list.generate(10, 100, 1000))
    print(len(linked_list))
