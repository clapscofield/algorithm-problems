"""
Leetcode Problem
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        neg = []
        for n in nums:
            neg.append(-n)
        
        heapq.heapify(neg)

        for i in range(k-1):
            heapq.heappop(neg)

        return -heapq.heappop(neg)
