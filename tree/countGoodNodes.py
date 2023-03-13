"""
Leetcode Problem
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        countGood = 0
        maxValue = root.val

        def dfs(node, maxValue):
            if not node:
                return 0
            
            #res indicates if it is goodNode or not
            res = 1 if maxValue <= node.val else 0
            maxValue = max(maxValue, node.val)
            
            #sum each res - if it is good node will be +1
            res += dfs(node.left, maxValue)
            res += dfs(node.right, maxValue)
            return res
        
        return dfs(root, maxValue)
            
