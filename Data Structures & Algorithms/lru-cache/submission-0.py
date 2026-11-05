from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lruCache = OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.lruCache:
            self.lruCache.move_to_end(key)
            return self.lruCache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.lruCache[key] = value
        self.lruCache.move_to_end(key)
        if self.capacity < len(self.lruCache):
            self.lruCache.popitem(last=False)
        
