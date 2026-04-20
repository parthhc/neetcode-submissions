class LRUCache:
    class LinkedList:
        class Node: 
            def __init__(self, key: int):
                self.key = key
                self.next = None
                self.prev = None

        def __init__(self):
            self.head = self.Node(0)
            self.tail = self.Node(0)
            self.head.next = self.tail
            self.tail.prev = self.head

        def add_last(self, node):
            prev, nxt = self.tail.prev, self.tail
            prev.next = nxt.prev = node
            node.prev, node.next = prev, nxt

        def remove(self, node):
            prev, nxt = node.prev, node.next
            prev.next, nxt.prev = nxt, prev

        def remove_first(self):
            # remove from head (LRU position)
            if self.head.next == self.tail:
                return None
            lru = self.head.next
            self.remove(lru)
            return lru

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}  # key -> (value, node)
        self.list = self.LinkedList()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        value, node = self.map[key]
        # move node to MRU
        self.list.remove(node)
        self.list.add_last(node)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # remove old node first
            _, node = self.map[key]
            self.list.remove(node)
        elif len(self.map) == self.capacity:
            # evict LRU
            lru = self.list.remove_first()
            if lru:
                del self.map[lru.key]

        # insert new node
        node = self.LinkedList.Node(key)
        self.list.add_last(node)
        self.map[key] = (value, node)
