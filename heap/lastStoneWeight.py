"""
Leetcode Problem
https://leetcode.com/problems/last-stone-weight/
"""

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones) #the first is the heaveist
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        
        stones.append(0) #when no stone
        return abs(stones[0])
