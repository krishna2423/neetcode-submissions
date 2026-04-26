class LRUCacheNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {} #supports o(1) get operations
        self.recent = LRUCacheNode(0, "recent")
        self.lru = LRUCacheNode(0, "lru")
        self.lru.next = self.recent
        self.recent.prev = self.lru

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].value
        else:
            return -1
    
    #remove from the list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    #insert at right
    def insert(self, node):
        old = self.recent.prev
        self.recent.prev = node
        node.next = self.recent
        node.prev = old
        old.next = node
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        self.hashmap[key] = LRUCacheNode(key, value)
        self.insert(self.hashmap[key])

        if len(self.hashmap) > self.capacity:
            least_recent = self.lru.next
            self.remove(least_recent)
            del self.hashmap[least_recent.key]

