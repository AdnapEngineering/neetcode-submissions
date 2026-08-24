class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map for key and nodes
        # dummy nodes for head and tail. Left = LRU and Right = MRU
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_node(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.add_node(node)
            return node.value
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove_node(node)
        else:
            new_node = Node(key,value)
            self.cache[key] = new_node

        self.add_node(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove_node(lru)
            del self.cache[lru.key]