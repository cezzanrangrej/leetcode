# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        if not root:
            return 0

        dq = deque([root])
        c = 0

        while dq:
            n = len(dq)

            for i in range(n):
                node = dq.popleft()

                if node.left:
                    dq.append(node.left)

                if node.right:
                    dq.append(node.right)

            c += 1

        return c