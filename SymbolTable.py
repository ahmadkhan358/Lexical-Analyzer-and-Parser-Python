class Node:
    def __init__(self, lexeme, token):
        self.lexeme = lexeme
        self.token = token
        self.next = None


class SymbolTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, lexeme):
        s = 0
        for letter in lexeme:
            s += ord(letter) * 9
        s %= self.size
        return s

    def insert(self, lexeme, token):
        if not self.lookup(lexeme):
            index = self._hash(lexeme)
            node = Node(lexeme, token)
            if self.table[index] is None:
                self.table[index] = node
            else:
                container = self.table[index]
                while container.next is not None:
                    container = container.next
                container.next = node

    def lookup(self, lexeme):
        index = self._hash(lexeme)
        if self.table[index] is not None:
            container = self.table[index]
            while True:
                if container == None:
                    return False

                if lexeme == container.lexeme:
                    break
                container = container.next
            return True
        else:
            return False

    def get(self, lexeme):
        return self.table[self._hash(lexeme)]
