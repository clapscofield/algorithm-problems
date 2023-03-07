"""
Leetcode Problem
https://leetcode.com/problems/insert-interval/
"""

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []

        for index, interval in enumerate(intervals):
            start = interval[0]
            end = interval[1]

            newStart = newInterval[0]
            newEnd = newInterval[1]

            #append in the beggining
            if newEnd < start:
                res.append(newInterval)
                return res + intervals[index:]
            
            #not overlap this curr interval, so we continue to check if 
            #overlaps with another
            elif newStart > end:
                res.append(interval)
            
            #is overlapping
            else:
                newInterval = [min(newStart, start), max(newEnd, end)]

        res.append(newInterval)
        return res
