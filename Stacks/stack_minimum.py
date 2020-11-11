class Item:

    def __init__(self, value=None):
        self.value = value
        self.min = None
        self.next = None

    def __str__(self):
        return "Value = {}, Min = {}".format(self.value, self.min)


class StackMin:

    def __init__(self):
        self.top = None

    def __iter__(self):
        node = self.top
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x) for x in self]
        return '\n'.join(values)

    def push(self, value):
        item = Item(value)
        # stack is empty
        if self.top is None:
            item.min = value
            self.top = item
            # stack not empty
        else:
            if value < self.top.min:
                item.min = value
            else:
                item.min = self.top.min
            item.next = self.top
            self.top = item

    def pop(self):
        # stack is empty
        if self.top is None:
            return "Stack is empty"
        else:
            item = self.top
            self.top = self.top.next
            return item

    def peek(self):
        if self.top is None:
            return "Stack is empty"
        else:
            return self.top

    def get_min(self):
        if self.top is None:
            return " Stack is empty"
        else:
            return self.top.min


stack = StackMin()
stack.push(3)
stack.push(2)
stack.push(5)
stack.push(1)
stack.push(7)
print(stack)
print("*" * 15)
stack.pop()
print(stack)
print(stack.get_min())
stack.pop()
print(stack)
print(stack.get_min())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
