class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None
        self.Prev = None

    def __repr__(self):
        return str(self.Data)

## Using Linkedlist 'sigle linked list - backward only'
class Queue:
    def __init__(self):
        self.Head = self.Tail = None

    def __repr__(self):
        print('Queue:')
        cur = self.Head
        while cur is not None:
            print(cur.Data)
            cur = cur.Next
        return ''

    def isEmpty(self):
        if self.Head is None:
            return True
        return False

    def Enqueue(self, data): # same as add in linked list
        nd = Node(data)
        if self.isEmpty():
            self.Head = self.Tail = nd
        else:  # add the node to be the tail 'append'
            self.Tail.Next = nd
            self.Tail = nd

    def Dequeue(self):
        nd = None
        if not self.isEmpty():
            nd = self.Head  # return first node
            self.Head = self.Head.Next
            if self.Head is None:  # check if the queue is empty after popping the first element
                self.Tail = None
        return nd



q = Queue()
q.Enqueue(10)
q.Enqueue(111)
print(q)
print(q.Dequeue())
print(q.Dequeue())
