class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete(self):
        if self.head is None:
            print("Stack is empty")
        else:
            value = self.head.value
            if self.head.next is None:
                self.head = None
                return value
            else:
                self.head = self.head.next
                return value

    def delete_list(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False


class Stack:

    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.linked_list]
        return '\n'.join(values)

    def push(self, value):
        self.linked_list.insert(value)

    def pop(self):
        if self.linked_list.is_empty():
            print("Stack is empty")
        else:
            return self.linked_list.delete()

    def peek(self):
        if self.linked_list.is_empty():
            print("Stack is empty")
        else:
            print(self.linked_list.head.value)

    def delete_stack(self):
        self.linked_list.delete_list()


stack_linked_list = Stack()
stack_linked_list.push(5)
stack_linked_list.push(10)
stack_linked_list.push(15)
stack_linked_list.peek()
print(stack_linked_list.pop())
stack_linked_list.peek()
stack_linked_list.pop()
stack_linked_list.peek()
