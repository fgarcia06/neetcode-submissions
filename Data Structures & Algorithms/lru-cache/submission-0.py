class Node:
    def __init__(self, key: int, value: int):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.mp = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        
        node = self.mp[key]
        self.remove(node)
        self.insert(node)

        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            # update the new node
            node = self.mp[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.mp[key] = node
            self.insert(node)
            if len(self.mp) > self.capacity:
                lru = self.left.next
                self.remove(lru)
                del self.mp[lru.key]
    
    def insert(self, node: Node):
        prev2 = self.right.prev
        prev2.next = node
        node.prev = prev2
        node.next = self.right
        self.right.prev = node

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
