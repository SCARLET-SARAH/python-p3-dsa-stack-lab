class Stack:
    def __init__(self, items=[], limit=100):
        self.items = items
        self.limit = limit
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def push(self, item):
        if self.top < self.limit - 1:
            self.items.append(item)
            self.top += 1
        else:
            raise Exception("Stack is full")

    def pop(self):
        if not self.isEmpty():
            item = self.items.pop()
            self.top -= 1
            return item
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if not self.isEmpty():
            return self.items[self.top]
        else:
            raise Exception("Stack is empty")

    def size(self):
        return self.top + 1

    def full(self):
        return self.top == self.limit - 1

    def search(self, target):
        for i in range(self.top, -1, -1):
            if self.items[i] == target:
                return self.top - i
        return -1