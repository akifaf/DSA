class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
f = Node(5)

a.next = b
b.next = c
c.next = d
d.next = f

def printlinkedlist(head):
    if head == None:
        return
    else:
        print(head.data)
        printlinkedlist(head.next)

printlinkedlist(a)

def linkedlistvalues(head, arr):
    if head == None:
        return
    else:
        arr.append(head.data)
        linkedlistvalues(head.next, arr)
        return arr
arr = []
print(linkedlistvalues(a, arr))