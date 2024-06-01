class BST:

    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

        
    def traverse(self):
        if self.lchild:
            self.lchild.traverse()
        print(self.key, end=", ")
        if self.rchild:
            self.rchild.traverse()

    def find_max(self):
        if self.key is None:
            return None
        if self.rchild is None:
            return print(self.key)
        if self.rchild:
            self.rchild.find_max()

    def find_min(self):
        if self.key is None:
            return None
        if self.lchild is None:
            return print(self.key)
        if self.lchild:
            self.lchild.find_min()

    def delete(self, value):
        if self.key is None:
            return None
        if value < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(value)
            else:
                return print("Not found")
        elif value > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(value)
            else:
                return print("Not found")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            min = self.rchild.find_min()
            self.key = min
            self.lchild.delete(min)
        return self


T = BST(45)
T.insert(2)
T.insert(4)
T.insert(3)
T.insert(65)
T.insert(42)
T.insert(76)
T.insert(41)
T.insert(47)
T.insert(99)
T.insert(25)
T.insert(22)
T.insert(75)
T.insert(53)
T.insert(35)
# T.find_max()
# T.find_min()
T.traverse()
print()
T.delete(2)
print()
T.traverse()