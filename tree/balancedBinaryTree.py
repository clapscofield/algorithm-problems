"""
Leetcode Problem
https://leetcode.com/problems/balanced-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(root): #return the [boolean check balanced, height]
            if not root:
                return [True, 0]
            right, left = dfs(root.right), dfs(root.left)
            balanced = (left[0] and right[0] and abs(right[1] - left[1]) <= 1)
            
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
