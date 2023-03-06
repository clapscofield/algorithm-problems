"""
Leetcode Problem
https://leetcode.com/problems/combination-sum/
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def backtracking(curr, comb, total):
            if total == target:
                res.append(list(comb))
                return

            if curr >= len(candidates) or total > target:
                return
            
            #include curr candidates 
            comb.append(candidates[curr])
            backtracking(curr, comb, total + candidates[curr])

            comb.pop()
            backtracking(curr + 1, comb, total)

        backtracking(0, [], 0)
        return res
