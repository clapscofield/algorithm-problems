"""
Leetcode Problem
https://leetcode.com/problems/validate-binary-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #right boundary and left boundary
        def checkSubtree(node, right, left):
            if not node:
                return True
            
            if not(node.val < right and node.val > left):
                return False
            
            return checkSubtree(node.left, node.val, left) and checkSubtree(node.right, right, node.val)
        

        return checkSubtree(root, float("inf"), float("-inf")) 
