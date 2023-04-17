class Node:
    def __init__(self,key,value):
        self.key=key
        self.val=value

        self.prev=self.next=None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity

        self.cache={}

        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left

    def remove(self,node):
        previous, nxt= node.prev, node.next
        nxt.prev=previous
        previous.next=nxt

    def insert(self,node):
        previous=self.right.prev
        nxt=self.right

        previous.next=node
        node.next=nxt
        nxt.prev=node
        node.prev=previous


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1    
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)    
        self.insert(self.cache[key])

        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)