class ListNode:
    def __init__(self, key = -1, value = -1, next=None):
        self.key = key
        self.val = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.size = 2069
        self.map = [ ListNode() for i in range(self.size)]
        

    def add_to_end(self, root, key, value):
        while root.next:
            root = root.next
        root.next = ListNode(key, value)

    def put(self, key: int, value: int) -> None:
        new_key = key%self.size
        temp = self.map[new_key]
        while temp:
            if temp.key == key:
                temp.val = value
                return
            temp = temp.next
        self.add_to_end(self.map[new_key], key, value)
        
    def search_linked_list(self, root, key):
        while root:
            if root.key == key:
                return root.val
            root = root.next
        return -1

    def get(self, key: int) -> int:
        new_key = key%self.size
        return self.search_linked_list(self.map[new_key], key)

    def remove_node_from_linked_list(self, root, key):
        prev = root
        cur = prev.next
        if cur.next:
            nxt = cur.next
        else:
            nxt = None
        while cur:
            if cur.key == key:
                prev.next = nxt
                return
            prev = prev.next
            cur = cur.next
            nxt = nxt.next
        
        return None

    def remove(self, key: int) -> None:
        new_key = key%self.size
        if self.search_linked_list(self.map[new_key], key) == -1:
            return None
        self.remove_node_from_linked_list(self.map[new_key], key)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)