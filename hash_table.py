# Hashtable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
#
# Name          : Leonardo Soriano
# Collaborators : 
# Time spent    : 

class HashTable:

    def __init__(self, size = 100):
        self.capacity = size 
        self.data = [None] * size
        self.values = [[] for _ in range(size)]
        self.size = 0

    def __getitem__(self, key):
        index = self.hash(key)
        for k, v in self.values[index]:
          if k == key:
            return v
        raise KeyError(key)
    
    def __setitem__(self, key, value):
        index = self.hash(key)

        for i, (key_exists, _) in enumerate(self.values[index]):
            if key_exists == key:
                self.values[index][i] = [key, value]
                return
        self.values[index].append([key, value])
        self.size += 1

    def set(self, key, value):
        self[key] = value

    def get(self,key):
        return self[key]
    
    def hash(self,key):
        return (hash(key) * (hash(key) +3)) % self.capacity
    
    def delete(self, key):
        index = self.hash(key)

        if not self.values[index]:
            raise KeyError(key)

        for i, (k, _) in enumerate(self.values[index]):
          if k == key:
             del self.values[index][i]
             self.size -= 1
             return

        raise KeyError(key)
    
    def __len__(self):
        return self.size


    
       

    
    