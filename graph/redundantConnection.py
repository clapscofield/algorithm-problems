"""
Leetcode Problem
https://leetcode.com/problems/redundant-connection/
"""

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def dfs(u,v):
            if u in visited:
                return False
            if u == v: #its a cycle, we get to the same point
                return True
            
            visited.add(u)
            
            #check the connected to the node u
            for i in graph[u]:
                if dfs(i, v):
                    return True
            return False
        
        
        n = len(edges)
        graph = defaultdict(set)
        
        ans = []
        #construct the graph and keep checking
        for u, v in edges:
            visited = set()
            if dfs(u, v): #dfs returns true if it is a cycle
                ans = [u,v] #save the answer and keep checking
            graph[u].add(v)
            graph[v].add(u)
        return ans
        
