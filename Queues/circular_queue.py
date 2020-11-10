class CircularQueue:

    def __init__(self, max_size):
        self.items = max_size * [None]
        self.max_size = max_size
        self.first = -1
        self.last = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def is_full(self):
        if self.last + 1 == self.first:
            return True
        elif self.first == 0 and self.last + 1 == self.max_size:
            return True
        else:
            return False

    def is_empty(self):
        if self.last == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.is_full():
            return "Queue is full"
        else:
            if self.last + 1 == self.max_size:
                self.last = 0
            else:
                self.last += 1
                if self.first == -1:
                    self.first = 0
            self.items[self.last] = value
            return "Item successfully enqueued"

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            dequeue_item = self.items[self.first]
            start = self.first
            if self.first == self.last:
                self.first = -1
                self.last = -1
            elif self.first + 1 == self.max_size:
                self.first = 0
            else:
                self.first += 1
            self.items[start] = None
            return dequeue_item

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.items[self.first]

    def delete(self):
        self.items = self.max_size * [None]
        self.first = -1
        self.last = -1


circular_queue = CircularQueue(10)
print(circular_queue.is_empty())
circular_queue.enqueue(1)
circular_queue.enqueue(2)
circular_queue.enqueue(3)
print(circular_queue)
print(circular_queue.dequeue())
print(circular_queue.dequeue())
print(circular_queue.dequeue())
print(circular_queue.peek())
