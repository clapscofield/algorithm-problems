"""
Leetcode Problem
https://leetcode.com/problems/non-overlapping-intervals/
"""

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        total = 0

        intervals.sort()
        print(intervals)
        prev = []
        for i in range(len(intervals)):
            if i == 0:
                prev = intervals[0]
            
            #not overlapping
            elif prev[0] >= intervals[i][1] or intervals[i][0] >= prev[1]:
                prev = intervals[i]
            
            #overlapps
            elif prev[0] <= intervals[i][0]:
                if prev[1] >= intervals[i][1]:
                    prev = intervals[i]
                total += 1

        return total 
