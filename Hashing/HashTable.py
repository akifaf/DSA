class Dictionary:

    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        
        hash_value = self.hash_function(key)

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value

            else:
                new_hash = self.rehash(hash_value)

                while self.slots[new_hash] != None and self.slots[new_hash] != key:
                    new_hash = self.rehash(new_hash)

                if self.slots[new_hash] == None:
                    self.slots[new_hash] = key
                    self.data[new_hash] = value
                
                if self.slots[new_hash] == key:
                    self.data[new_hash] = value

    def rehash(self, old_hash):
        return old_hash + 1

    def hash_function(self, key):

        return abs(hash(key)) % self.size
    

D1 = Dictionary(3)

print(D1.slots)
print(D1.data)