class Stack:

    def __init__(self, size):
        self.list = []
        self.size = size

    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False

    def is_full(self):
        if len(self.list) == self.size:
            return True
        else:
            return False

    def push(self, value):
        if self.is_full():
            return "The stack is full"
        else:
            self.list.append(value)
            return "Item successfully added to stack"

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.list[len(self.list - 1)]


stack_list = Stack(5)
print(stack_list.peek())
