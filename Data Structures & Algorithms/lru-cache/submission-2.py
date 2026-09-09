class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        left, right = node.prev, node.next
        left.next = right
        right.prev = left

    def insert(self, node):
        last, second_last = self.right, self.right.prev
        last.prev = node
        second_last.next = node
        node.prev = second_last
        node.next = last

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)

        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = new_node
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            key_to_remove = self.left.next.key
            self.remove(self.cache[key_to_remove])
            del self.cache[key_to_remove]

