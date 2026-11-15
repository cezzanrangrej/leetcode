# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        from collections import deque
        
        if not root:
            return []

        dq=deque([root])
        result=[]

        while dq:
            n=len(dq)
            level=[]

            for i in range(n):
                node=dq.popleft()
                level.append(node.val)

                if node.left:
                    dq.append(node.left)

                if node.right:
                    dq.append(node.right)
            result.append(level)
        return result[::-1]