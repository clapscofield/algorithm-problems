"""
Leetcode problem
https://leetcode.com/problems/binary-tree-right-side-view/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        queue = collections.deque([root])

        while queue:
            rightSide = None
            qLen = len(queue)

            for i in range(qLen): #every node in the current level
                node = queue.popleft()
                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightSide:
                res.append(rightSide.val)

        # end

        return res
