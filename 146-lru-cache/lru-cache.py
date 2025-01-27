class Node:
    def __init__(self,key ,val = None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.capacity = capacity
        self.left.next, self.right.prev = self.right, self.left

    # add at right, as LRU is at left
    def insert (self,node):
        prev, nxt = self.right.prev, self.right
        prev.next=  nxt.prev = node
        node.prev,node.next = prev, nxt
    
    def remove (self,node):
        # return val
        prev,nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        

    def get(self, key: int) -> int:
        # make it mru
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            node = self.cache[key]
            return node.val

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        # add new keh
        self.insert(self.cache[key])
        if (len(self.cache) >self.capacity ):
            # remove lru
            lru = self.left.next
            self.remove(lru)
            # that what store key in nOde alongw ith value
            del self.cache[lru.key]

            

            
        

        
# Q what if key exits in put
# how to do ?

# make key as the input & value as Node. Use double link list


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)