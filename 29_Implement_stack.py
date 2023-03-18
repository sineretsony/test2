class Stack:
    def __init__(self):
        self.init_list = []

    def push(self, item):
        self.init_list.append(item)

    def pop(self):
        if len(self.init_list) > 0:
            return self.init_list.pop()
        else:
            return None

    def empty(self):
        return len(self.init_list) == 0

    def peek(self):
        if len(self.init_list) > 0:
            return self.init_list[-1]
        else:
            return None


stack_full = Stack()

stack_full.push(10)
stack_full.push(20)
stack_full.push(30)

print("Чи порожній стек? ", stack_full.empty())
print("Видалений останній елемент: ", stack_full.pop())
print("Останній елемент у стеку", stack_full.peek())

stack_empty = Stack()

print("Чи порожній стек? ", stack_empty.empty())
print("Уалённий останній елемент у порожньому: ", stack_empty.pop())
print("Останній елемент у порожньому стеку", stack_empty.peek())

print("Стек 'повний' ", stack_full.init_list)



