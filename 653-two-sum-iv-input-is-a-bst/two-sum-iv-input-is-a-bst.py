# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def fun(node,path):
            if not node:
                return False
            find=k-node.val
            if find in path:
                return True

            path.append(node.val)
            return fun(node.left,path) or fun(node.right, path)
        return fun(root,[])
