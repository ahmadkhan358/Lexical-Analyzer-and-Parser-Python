class Stack:
    def __init__(self):
        self.top = -1
        self.st = []

    def push(self, value):
        self.st.append(value)
        self.top += 1

    def pop(self):
        temp = self.st[self.top]
        self.st.pop()
        self.top -= 1
        return temp

    def get_top(self):
        return self.st[self.top]

    def print_stack(self):
        for i in self.st:
            print(i)



