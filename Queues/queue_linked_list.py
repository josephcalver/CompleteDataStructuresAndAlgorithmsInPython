class Node:

    def __init__(self, value=None):
        self.value = value
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
        values = [str(x) for x in self]
        return ' '.join(values)

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def remove(self):
        if self.head is None:
            return
        else:
            node = self.head
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return node

    def get(self):
        if self.head is None:
            return
        else:
            return self.head.value

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False


class Queue:

    def __init__(self):
        self.queue = LinkedList()

    def __iter__(self):
        node = self.queue.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.value) for x in self.queue]
        return ' '.join(values)

    def enqueue(self, value):
        return self.queue.add(value)

    def dequeue(self):
        return self.queue.remove()

    def peek(self):
        return self.queue.get()

    def is_empty(self):
        return self.queue.is_empty()


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue)
print(queue.peek())
print(queue.dequeue())
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(queue.peek())
queue.enqueue('Joseph')
# queue.enqueue('Caolan')
# queue.enqueue('Freya')
print(queue.peek())
queue.dequeue()
print(queue.peek())
