class Node:
    def __init__(self, data):
        self.Data = data
        self.Prev = None

    def __repr__(self):
        return str(self.Data)

## Using Linkedlist 'sigle linked list - backward only'
class Stack:
    def __init__(self):
        self.Tail = None

    def __repr__(self):
        cur = self.Tail
        while cur is not None:
            print(cur.Data)
            cur = cur.Prev
        return ''

    def isEmpty(self):
        if self.Tail is None:
            return True
        return False

    def Push(self, n):
        nd = Node(n)
        if self.isEmpty():  # empty
            self.Tail = nd
        else:
            nd.Prev = self.Tail
            self.Tail = nd

    def Pop(self):
        nd = None
        if not self.isEmpty():
            nd = self.Tail
            self.Tail = self.Tail.Prev
        return nd

## Using array
class Stack_by_array:
    def __init__(self):
        self.arr = []

    def __repr__(self):
        print(self.arr)
        return ''

    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        return False

    def Push(self, n):
        self.arr.append(n)

    def Pop(self):
        nd = None
        if not self.isEmpty():
            nd = self.arr.pop()
        return nd


s = Stack()
# s = Stack_by_array()
s.Push(1)
s.Push(2)
s.Push(3)

print(s)

print('pop:' , s.Pop())
print('pop:' , s.Pop())
print('pop:' , s.Pop())
print('pop:' , s.Pop())

