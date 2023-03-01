"""
Leetcode problem
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #Use the values to check if it goes to left or right
        # If there is a split of subtree, we found the LCA

        cur = root

        while cur:
            if cur.val > q.val and cur.val > p.val:
                cur = cur.left
            elif cur.val < q.val and cur.val < p.val:
                cur = cur.right
            else:
                return cur
