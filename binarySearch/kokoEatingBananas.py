"""
Leetcode Problem
https://leetcode.com/problems/koko-eating-bananas/
"""

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def ceildiv(a, b):
            return -(a // -b)

        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += ceildiv(p, k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res
