"""
Leetcode Problem
https://leetcode.com/problems/top-k-frequent-elements/
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counting = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            counting[n] = 1 + counting.get(n, 0)

        for number, count in counting.items():
            freq[count].append(number)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
        
