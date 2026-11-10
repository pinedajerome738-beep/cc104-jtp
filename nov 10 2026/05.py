class node:
    def _init_(self, value):
        self.value = value
        self.next = None
a = node(10)
b = node(20)
a.next = b
print(a.next.value)