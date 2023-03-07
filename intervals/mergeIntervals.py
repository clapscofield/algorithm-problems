"""
Leetcode Problem
https://leetcode.com/problems/merge-intervals/
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort() #this sorts by the first element of each list

        res = []
        newMerged = []
        for index, interval in enumerate(intervals):
            #the first one
            if len(newMerged) == 0:
                newMerged = [interval[0], interval[1]]

            elif newMerged[1] >= interval[0]:
                newMerged = [min(newMerged[0], interval[0]), max(newMerged[1], interval[1])]
            
            elif newMerged[1] < interval[0]:
                res.append(newMerged)
                newMerged = [interval[0], interval[1]]
                
        res.append(newMerged)
        return res
