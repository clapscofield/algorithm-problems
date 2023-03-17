"""
Leetcode Problem
https://leetcode.com/problems/lru-cache/
"""

class Node(object):
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)

        #left LRU
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def  insert(self, node):
        prevright = self.right.prev
        prevright.next, node.prev = node, prevright
        self.right.prev, node.next = node, self.right

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key]) #remove from the actual position
            self.insert(self.cache[key]) #insert into the right most position (recent used)
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        #check capacity and remove if necessary
        if len(self.cache) > self.capacity:
            #remove lru -> saved in left.next
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
