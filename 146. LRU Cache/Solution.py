# My not-O(1) solution
class LRUCache:

    def __init__(self, capacity: int):
        self.storage = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        i = len(self.storage) - 1
        FOUND = False
        while i >= 0:
            if self.storage[i][0] == key:
                recent = self.storage.pop(i)
                FOUND = True
                break
            i -= 1
        if FOUND:
            self.storage.append(recent)
            return recent[1]
        else:
            return -1
                
    def put(self, key: int, value: int) -> None:
        found_val = self.get(key)
        if found_val == -1:
            if len(self.storage) == self.capacity:
                self.storage.pop(0)             
            self.storage.append((key, value))
        else:
            self.storage[-1] = (key, value)
            
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Using OrderedDict
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)  
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False)  
        else:
            self.cache.move_to_end(key) 
        self.cache[key] = value