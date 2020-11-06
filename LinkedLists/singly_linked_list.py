class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value, location):
        new_node = Node(value)
        #   list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #   insert at beginning
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == -1:
                # new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            #     delete from index
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                temp_node.next = new_node

    def delete(self, location):
        if self.head is None:
            print("The list is empty")
        else:
            # delete from beginning
            if location == 0:
                # if only one element in list
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head = self.head.next
                else:
                    self.head = self.head.next
            # delete from end
            elif location == - 1:
                previous_node = self.head
                while previous_node.next is not self.tail:
                    previous_node = previous_node.next
                previous_node.next = None
                self.tail = previous_node
            #      delete from index
            else:
                previous_node = self.head
                index = 0
                while index < location - 1:
                    previous_node = previous_node.next
                    index += 1
                node_to_delete = previous_node.next
                print("{}, {}".format(previous_node.value, node_to_delete.value))
                previous_node.next = node_to_delete.next

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

    def find(self, value):
        if self.head is None:
            print("List is empty")
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == value:
                    print("Item with value {} exists".format(value))
                    break
                temp_node = temp_node.next
            else:
                print("Item with value {} does not exist".format(value))


singly_linked_list = SinglyLinkedList()
singly_linked_list.insert(1, -1)
singly_linked_list.insert(2, -1)
singly_linked_list.insert(3, -1)
singly_linked_list.insert(4, -1)
singly_linked_list.insert(0, 0)
singly_linked_list.insert(99, 3)
singly_linked_list.insert(111, 1)
singly_linked_list.traverse()
print([node.value for node in singly_linked_list])
singly_linked_list.find(99)
singly_linked_list.find(222)
print([node.value for node in singly_linked_list])
singly_linked_list.delete(4)
print([node.value for node in singly_linked_list])
singly_linked_list.delete_list()
