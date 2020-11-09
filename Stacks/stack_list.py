class Stack:

    def __init__(self):
        self.list = []

    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
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
            return self.list[len(self.list) - 1]


stack_list = Stack()
stack_list.push(1)
stack_list.push(2)
stack_list.push(3)
# print(stack_list)
print(stack_list.peek())
print(stack_list.pop())
print(stack_list.peek())
