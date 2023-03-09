"""
Leetcode Problem
https://leetcode.com/problems/course-schedule/
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) == 0:
            return True

        #turn prerequisits into a dict
        adjlist = {i: [] for i in range(numCourses)}
        for ai, bi in prerequisites:
            adjlist[ai].append(bi)

        visit = set()

        def dfs(v):
            #already visited
            if v in visit:
                return False
           
           #there is no prereq to do this course
            if adjlist[v] == []:
                return True

            visit.add(v)
            for prereq in adjlist[v]:
                if not dfs(prereq):
                    return False

            #if we visited all prereq and none was already visited
            # there is no cycle, so we pass to another v and return
            #true to this v 
            visit.remove(v)
            adjlist[v] = []
            return True

        for v in range(numCourses):
           if not dfs(v):
               return False

        return True


 


