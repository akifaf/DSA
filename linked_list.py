# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.n = 0

#     # length of linked list
#     def __len__(self):
#         return self.n

#     def insert_head(self, value):
#         # new node
#         new_node = Node(value)

#         # create connection
#         new_node.next = self.head

#         # reassign head
#         self.head = new_node

#         #increment length
#         self.n += 1

#     def __str__(self):
#         curr = self.head
#         result = " "
#         while curr != None:
#             result = result + str(curr.data) + "->"
#             curr = curr.next
#         return result[:-2]

#     def add(self, value):

#         new_node = Node(value)

#         if self.head == None:
#             self.head = new_node
#             self.n += 1
#             return

#         curr = self.head

#         while curr.next != None:
#             curr = curr.next

#         curr.next = new_node
#         self.n += 1

#     def insert_after(self, after, value):

#         new_node = Node(value)

#         curr = self.head

#         while curr != None:
#             if curr.data == after:
#                 break
#             curr = curr.next

#         if curr != None:
#             new_node.next = curr.next

#             curr.next = new_node
#         else:
#             return "Item not found"

#     def insert_before(self, before, value):

#         new_node = Node(value)

#         curr = self.head
#         prev = None

#         while curr != None:
#             if curr.data == before:
#                 break
#             prev = curr
#             curr = curr.next

#         if curr != None:
#             new_node.next = curr
#             self.n += 1
#             if prev != None:
#                 prev.next = new_node
#             else:
#                 self.head = new_node
#         else:
#             print('not found')

#     def clear(self):
#         self.head = None
#         self.n = 0

#     def delete_head(self):
#       if self.head == None:
#         return "Empty ll"
#       self.head = self.head.next
#       self.n -=1

#     def pop(self):

#       if self.head == None:
#         return "Empty ll"

#       curr = self.head

#       if curr.next == None:
#         self.delete_head()
#         return

#       while curr.next.next != None:
#         curr = curr.next

#       curr.next = None
#       self.n -= 1

#     def remove(self, value):

#       curr = self.head

#       while curr.next != None:
#         if curr.next.data == value:
#           break
#         curr = curr.next

#       if curr.next == None:
#         return "Not found"
#       else:
#         curr.next = curr.next.next

#     def search(self, value):

#       curr = self.head
#       pos = 0

#       while curr != None:
#         if curr.data == value:
#           return pos
#         curr = curr.next
#         pos += 1
#       return "not found"

#     def __getitem__(self, index):

#       curr = self.head
#       pos = 0

#       while curr != None:
#         if pos == index:
#           return curr.data
#         curr = curr.next
#         pos += 1
#       return "IndexError"

#     def replace_max(self, value):

#       temp = self.head

#       max = temp

#       while temp != None:
#         if temp.data > max.data:
#           max = temp
#         temp = temp.next

#       max.data = value

#     def sum_odd_nodes(self):

#       temp = self.head
#       pos = 0
#       sum = 0

#       while temp != None:
#         if pos % 2 != 0:
#           sum += temp.data
#         temp = temp.next
#         pos += 1
#       return sum

#     def reverse(self):

#       curr_node = self.head
#       prev_node = None

#       while curr_node != None:
#         next_node = curr_node.next
#         curr_node.next = prev_node
#         prev_node = curr_node
#         curr_node = next_node

#       self.head = prev_node

#       #  The/*sky*is//blue

#     def change_sent(self):

#       temp = self.head

#       while temp != None:
#         if temp.data == '*' or temp.data == '/':
#           temp.data = ' '
#           if temp.next.data == '*' or temp.next.data == '/':
#             temp.next.next.data = temp.next.next.data.upper()
#             temp.next = temp.next.next
#         temp = temp.next

    



class Node:
   
   def __init__(self, value):
      self.data = value
      self.next = None

class Linkedlist:
    
    def __init__(self):
       self.head = None
       self.n = 0

    def __len__(self):
       pass


    def insert_head(self, value):
    
      new_node = Node(value)

      new_node.next = self.head

      self.head = new_node

      self.n += 1

    def __str__(self):
       
      result = ""

      curr = self.head

      while curr != None:
        result += '->' + str(curr.data)
        curr = curr.next 

      return result[2:]

    def add(self, value):
      
      new_node = Node(value)

      curr = self.head
      


    def insert_after(self, after, value):
      pass


    def insert_before(self, before, value):
      pass


    def clear(self):
      pass


    def delete_head(self):
      pass


    def pop(self):
      pass


    def remove(self, value):
      pass


    def search(self, value):
      pass


    def __getitem__(self, index):
      pass


    def replace_max(self, value):
      pass


    def sum_odd_nodes(self):
      pass


    def reverse(self):
      pass


    def change_sent(self):
      pass

L = Linkedlist()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(5)
print(L)