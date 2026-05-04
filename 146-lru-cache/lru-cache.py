class ListNode:
        def __init__(self, key=0, val=0, l=None, r=None):
            self.key = key
            self.val = val
            self.l=l
            self.r=r

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1,-1)
        self.head.r = self.tail
        self.tail.l = self.head
        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]
        self.remove_node(node)
        self.insert_new_node_before_tail(node, self.tail)
        return node.val 

    def remove_node(self, root):
        prev = root.l
        next = root.r
        prev.r = next
        root.r = None
        next.l = prev
        root.l = None

    def insert_new_node_before_tail(self, node, tail):
        prev = tail.l
        prev.r = node
        node.l = prev
        node.r = tail
        tail.l = node    

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].val = value
            self.remove_node(self.map[key])
            self.insert_new_node_before_tail(self.map[key], self.tail)
        else:
            if len(self.map) >= self.capacity:
                del self.map[self.head.r.key]
                self.remove_node(self.head.r)
            new_node = ListNode(key, value)
            self.map[key] = new_node
            self.insert_new_node_before_tail(self.map[key], self.tail)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)