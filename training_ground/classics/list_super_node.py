class Node:
    def __init__(self, data) -> None:
        self.previous = None
        self.data = data
        self.next = None

    def append(self, val):
        end = Node(val)
        n = self
        while (n.next):
            n = n.next
        n.next = end
        end.previous = n

    def first(self):
        while self.previous:
            self = self.previous
        return self


ll = Node(1)
ll.append(2)
ll.append(3)
node = ll
for i in range(4, 21):
    node.append(i)
print(node.data)
while node.next:
    node = node.next
    print(node.data)
print(node.data)
node = node.first()
print(node.data)
# while node.previous:
#     node = node.previous
#     print(node.data)
# print(node.data)
