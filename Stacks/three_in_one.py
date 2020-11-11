class MultiStack:

    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.num_stacks = 3
        self.multistack_list = [0] * (self.stack_size * self.num_stacks)
        self.stack_counters = [0] * self.num_stacks

    def is_full(self, stack_num):
        if self.stack_counters[stack_num - 1] == self.stack_size:
            return True
        else:
            return False

    def is_empty(self, stack_num):
        if self.stack_counters[stack_num - 1] == 0:
            return True
        else:
            return False

    def index_of_top(self, stack_num):
        offset = (stack_num - 1) * self.stack_size
        return offset + self.stack_counters[stack_num - 1]

    def push(self, stack_num, value):
        if self.is_full(stack_num):
            return "Stack {} is full".format(stack_num)
        else:
            self.multistack_list[self.index_of_top(stack_num)] = value
            self.stack_counters[stack_num - 1] += 1

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            return "Stack {} is empty".format(stack_num)
        else:
            value = self.multistack_list[self.index_of_top(stack_num)]
            self.multistack_list[self.index_of_top(stack_num)] = 0
            self.stack_counters[stack_num - 1] -= 1
            return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            return "Stack {} is empty".format(stack_num)
        else:
            return self.multistack_list[self.index_of_top(stack_num)]


multistack = MultiStack(3)
multistack.push(1, 1)
multistack.push(1, 2)
multistack.push(1, 3)
print(multistack.multistack_list)
print(multistack.is_full(1))
multistack.push(2, 4)
multistack.push(2, 5)
multistack.push(2, 6)
print(multistack.push(2, 7))
print(multistack.multistack_list)
print(multistack.is_empty(3))
