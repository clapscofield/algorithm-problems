"""
Leetcode Problem
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = deque()
        output = []

        def bfs(node):
            q.append(node)
            sub = []

            while q:
                for i in range(len(q)):
                    element = q.popleft()
                    sub.append(element.val)

                    if element.left: 
                        q.append(element.left)
                    if element.right: 
                        q.append(element.right)

                output.append(sub)
                sub = []

        if root:
            bfs(root)
        return output
