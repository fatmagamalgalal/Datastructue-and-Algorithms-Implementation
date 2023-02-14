class Node:
    def __init__(self, val):
        self.value = val
        self.Next = None
        self.Prev = None

    def __repr__(self):
        return str(self.value)


# double linked list #
# we have 3 cases:
#     1 - linkedlist is empty -> Head = None
#     2 - linkedlist has one node
#     3 - linkedlist has many nodes

class LinkedList:
    def __init__(self):
        self.Head = self.Tail = None

    def __repr__(self):
        print('List: ')
        cur = self.Head
        while cur != None:
            print(cur.value)
            cur = cur.Next
        return ''

    def isEmpty(self):
        if self.Head is None:
            return True
        return False

    def add_node(self, data):
        nd = Node(data)
        if self.isEmpty():
            self.Head = self.Tail = nd
        else:  # add the node to be the tail 'append'
            self.Tail.Next = nd
            nd.Prev = self.Tail
            self.Tail = nd

    def insert_node(self, data, loc):  # we should insert the node to be at index = loc
        nd = Node(data)
        if self.isEmpty():
            self.Head = self.Tail = nd
        else:
            if loc == 0:
                self.Head.Prev = nd
                nd.Next = self.Head
                self.Head = nd
            else:  # search for the node at loc - 1
                i = 0
                cur = self.Head
                while i < loc - 1 and cur.Next is not None:  # we stop at the node that we will insert after
                    cur = cur.Next
                    i += 1
                # we now have the position of the node, we will insert after it
                if cur == self.Tail:  # append
                    self.Tail.Next = nd
                    nd.Prev = self.Tail
                    self.Tail = nd
                else:  # add in between
                    cur.Next.Prev = nd
                    nd.Next = cur.Next
                    nd.Prev = cur
                    cur.Next = nd

    def search(self, data):
        nd = None
        if not self.isEmpty():
            nd = self.Head
            while nd is not None and nd.value != data:
                nd = nd.Next
        return nd

    def delete_node(self, loc):  # the same idea of insert
        retVal = 0  # return 1 if deleted successfully, 0 if not
        cur = None
        if not self.isEmpty():
            cur = self.Head
            if loc == 0:
                if self.Head == self.Tail:  # the list has only 1 node
                    self.Head = self.Tail = None
                else:
                    self.Head = self.Head.Next
                    self.Head.Prev = None
                retVal = 1
            else:  # search for the node at loc
                i = 0
                while i < loc and cur is not None:  # we stop at the node that we will delete
                    cur = cur.Next
                    i += 1
                # we now have the position of the node we will delete
                if cur is not None:
                    if cur == self.Tail:  # delete last node
                        self.Tail = self.Tail.Prev
                        self.Tail.Next = None
                    else:  # in between
                        cur.Next.Prev = cur.Prev
                        cur.Prev.Next = cur.Next
                    retVal = 1
        return retVal


ll = LinkedList()

# add nodes
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)

# insert nodes
# ll.insert_node(10, 0)
# ll.insert_node(10, 1)
# ll.insert_node(10, 2)
ll.insert_node(10, 4)

print(ll)

# search for a node
# print(ll.search(10))

# delete node
# res = ll.delete_node(0)
# res = ll.delete_node(1)
res = ll.delete_node(3)
# res = ll.delete_node(4)
print(res)
print(ll)

