"""
Leetcode Problem
https://leetcode.com/problems/time-based-key-value-store/
"""

class TimeMap(object):

    def __init__(self):
        self.timemap = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key in self.timemap:
            self.timemap[key].append([value, timestamp])
        else:
            self.timemap[key] = [[value, timestamp]]        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res = ""
        keyarray = self.timemap.get(key, [])
        l, r = 0, len(keyarray) - 1

        while l <= r:
            middle = (l + r)//2
            if keyarray[middle][1] <= timestamp:
                res = keyarray[middle][0]
                l = middle + 1
            else:
                r = middle - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
