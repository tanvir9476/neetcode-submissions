class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key: Node
        self.LRU, self.MRU = Node(None, None), Node(None, None)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
    def remove(self, node):
        nxt, prv = node.next, node.prev
        prv.next = nxt
        nxt.prev = prv
    def insert_right(self, node):
        nxt, prv = self.MRU, self.MRU.prev
        prv.next = node
        nxt.prev = node
        node.prev = prv
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert_right(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert_right(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.LRU.next
            self.remove(lru)
            del self.cache[lru.key]