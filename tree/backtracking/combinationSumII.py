"""
Leetcode Problem

"""

#Fisrt try - Time Limit exceed
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()

        candidates.sort()
        def backt(subsetTotal, curr):
            if subsetTotal[1] == target:
                res.add(tuple(subsetTotal[0]))
                return

            if curr >= len(candidates) or subsetTotal[1] > target:
                return

            subsetTotal[0].append(candidates[curr])
            subsetTotal[1] += candidates[curr]
            backt(subsetTotal, curr + 1)

            subsetTotal[0].pop()
            subsetTotal[1] -= candidates[curr]
            backt(subsetTotal, curr + 1)
        
        backt([[], 0], 0)
        return list(map(list, res))

#Correct version
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()

        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(list(cur))
                return
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res
