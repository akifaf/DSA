# class Node:

#     def __init__(self, value):
#         self.data = value
#         self.next = None

# class Stack:

#     def __init__(self):
#         self.top = None

#     def push(self, value):
        
#         new_node = Node(value)

#         new_node.next = self.top

#         self.top = new_node

#     def isEmpty(self):
#         return self.top == None
    
#     def pop(self):
        
#         if self.isEmpty():
#             return "Empty stack"
        
#         self.top = self.top.next

#     def traverse(self):
        
#         temp = self.top

#         while temp != None:
#             print(temp.data)
#             temp = temp.next


#     def peek(self):

#         if self.isEmpty():
#             return "Empty stack"
        
#         print(self.top.data)

         
# s = Stack()
# s.push(4)
# s.push(3)
# s.push(2)
# s.push(1)
# s.traverse()
# s.pop()
# s.pop()
# s.traverse()
        

# class Stack:

#     def __init__(self, size):
#         self.size = size
#         self.stack = [None] * self.size
#         self.top = -1

#     def push(self, value):

#         if self.top == self.size:
#             return print("Overflow")
        
#         self.top += 1
#         self.stack[self.top] = value

#     def pop(self):

#         if self.top == -1:
#             return print("Empty")
        
#         else:
#             data = self.stack[self.top]
#             # print(data)
#             self.top -= 1

#     def traverse(self):

#         while self.top != -1:
#             print(self.stack[self.top], end=" ")
#             self.top -= 1

# s = Stack(4)
# s.push(4)
# s.push(3)
# s.push(2)
# s.push(1)

# s.pop()
# s.pop()
# s.pop()
# s.traverse()


# Balanced Paranthesis

text = '[]}'

def parenthesis(text):
    stack = []
    dict = {"(":")", "{":"}", "[":"]"}

    for i in text:
        if i in dict:
            stack.append(i)
        else:
            if stack and dict[stack[-1]] == i:
                stack.pop()
            else:
                return False
    
    return False if stack else True

# print(parenthesis(text))

text = "/home//foo/../house/./heaven//"

def simplest_path(text):
    stack = []
    curr = ""

    for i in text + '/':
        if i == '/':
            if curr == '..':
                if stack: stack.pop()
            elif curr != "" and curr != '.':
                stack.append(curr)
            curr = ""
        else:
            curr += i
        
    return '/' + '/'.join(stack)


# print(simplest_path(text))

from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        
        for i in range(len(self.queue)-1):
            popped = self.queue.popleft()
            self.queue.append(popped)
            self.display()
        return self.queue.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return True if self.queue else False
    
    def display(self):
        print(self.queue)


# # Your Myqueue object will be instantiated and called as such:
# obj = MyStack()
# obj.display()
# param_2 = obj.pop()
# print(param_2)
# obj.display()
# # param_3 = obj.top()
# param_4 = obj.empty()
# print(param_4)

class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.stack1 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        

    def pop(self):

        if not self.stack1:
            while self.stack:
                self.stack1.append(self.stack.pop())
        return self.stack1.pop()    
        


    def peek(self):
        """
        :rtype: int
        """
        return print(self.stack[-1])
        

    def empty(self):
        """
        :rtype: bool
        """
        return (len(self.stack)) == 0

    def display(self):
        return print(self.stack)

# Your MyQueue object will be instantiated and called as such:
    
obj = MyQueue()
obj = MyQueue()
obj.push(1)
# param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

