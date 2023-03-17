"""
Leetcode Problem
https://leetcode.com/problems/course-schedule-ii/
"""

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        #[[1,0], [2,0], [3,1], [3,2]]
        # 3 -> 1 -> 0
        #   -> 2 ->
        # 0, 2, 1, 3 or 0, 1, 2, 3

        # create an adj list to represent the graph
        adj = {i: [] for i in range(numCourses)}
        for ai, bi in prerequisites:
            adj[ai].append(bi)


        # run a dfs in every single node and go further to the prereq.
        # when i found one that has no pre req i can return
        visit, cycle = set(), set()
        order = []

        def dfs(node):
            #check if is impossible to finish all
            if node in cycle:
                return False

            #is not a cycle and we already added to the output
            if node in visit:
                return True

            #not a cycle and yet not added to the output
            cycle.add(node)
            for pre in adj[node]:
                if not dfs(pre):
                    return False
            
            cycle.remove(node)
            visit.add(node)
            order.append(node)
            return True

        
        for v in range(numCourses):
            if not dfs(v):
                return []
        
        return order
