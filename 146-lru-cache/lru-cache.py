class ListNode:
    def __init__(self, key , value):
        self.val = value
        self.key = key
        self.prev = self.next = None
class LRUCache:
    
        

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        prev,nxt = node.prev, node.next
        prev.next  = nxt
        nxt.prev = prev



    def insert(self,node) :  
        prev, nxt = self.right.prev, self.right
        prev.next= nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = ListNode(key,value)
        self.cache[key]=node
        self.insert(node)
        # insert

        if len(self.cache) > self.capacity :
            lru = self.left.next
            self.remove(lru)
            # remove key also
            del self.cache[lru.key]
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)