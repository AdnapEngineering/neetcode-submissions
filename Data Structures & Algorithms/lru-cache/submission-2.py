class Node: # double linked list
    def __init__(self, key , value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # dic to keep track of nodes

        # need dummy / sentinal nodes
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def remove_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_node(self,node):
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
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            node = self.cache[key]
            node.value = value
            self.remove_node(node)
            self.add_node(node)
        else:               
            if len(self.cache) == self.capacity: 
                lru = self.head.next
                self.remove_node(lru)
                del self.cache[lru.key]
            node = Node(key, value)
            self.cache[key] = node
            self.add_node(node)
        
