class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class Stack:

    def __init__(self) -> None:
        self.top = None

    def isEmpty(self):
        if self.top == None:
            return True
        return False
    
    def push(self, key):
        new_node = Node(key)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        
        curr = self.top
        self.top = self.top.next
        return curr.key
    
    def traverse(self):
        
        curr = self.top
        while curr != None:
            print(curr.key)
            curr = curr.next

    def peek(self):

        if self.isEmpty() == True:
            return print("Empty stack")
        
        return print(self.top.key)

def reverse_string(string):
    S = Stack()

    for i in string:
        S.push(i)

    result = ''
    while not S.isEmpty():
        result += S.pop()

    print(result)

def undo_redo(string, pattern):

    undo = Stack()
    redo = Stack()

    for i in string:
        undo.push(i)

    for i in pattern:
        if i == 'u':
            letter = undo.pop()
            redo.push(letter)
        else:
            letter = redo.pop()
            undo.push(letter)

    return undo.traverse()

# undo_redo('kolkata', 'uurruru')

def balanced_parenthesis(s):

    paranthesis = {'}':'{', ')':'(', ']':'['}
    stack = []
    for i in s:
        if i in paranthesis:
            if stack and stack.pop() == paranthesis[i]:
                pass
            else:
                return False
        else:
            stack.append(i)

    return True if not stack else False



print(balanced_parenthesis('[]]'))