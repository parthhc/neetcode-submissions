class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mapp = {}

        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.nxt, self.right.prev = self.right, self.left
        

    def get(self, key: int) -> int:
        if key not in self.mapp: return -1

        node = self.mapp[key]
        res = node.value
        self.remove_node(node)
        self.insert_node(node)

        return res

    def remove_node(self, node) -> None:
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def insert_node(self, node) -> None:
        prev, nxt = self.left, self.left.nxt
        node.prev, node.nxt = prev, nxt
        prev.nxt = node
        nxt.prev = node
    
    
    def put(self, key: int, value: int) -> None:
        if key in self.mapp:
            node = self.mapp[key]
            node.value = value
            self.remove_node(node)
            self.insert_node(node)
        else:
            if len(self.mapp) >= self.cap:
                node_to_del = self.right.prev
                self.remove_node(node_to_del)
                del self.mapp[node_to_del.key]
            
            new_node = Node(key, value)
            self.insert_node(new_node)
            self.mapp[key] = new_node


        
