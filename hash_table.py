# Hashtable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
#
# Name          : Leonardo Soriano
# Collaborators : 
# Time spent    : 


class HashTable:

    def __init__(self, size=100):
        self.capacity = size
        self.data = [None] * size

    def __getitem__(self, key):
        index = hash(key) % self.capacity
        if self.data[index] is None:
            raise KeyError("KeyError: Key not found")
        return self.data[index]
    
    def __setitem__(self, key, value):
        index = hash(key) % self.capacity
        self.data[index] = value
        

    def set(self, key, value):
        self[key] = value

    def get(self,key):
        return self[key]
    
    def hash(self, key):
        return(hash(key) * (hash(key) +3)) % self.capacity

    
    