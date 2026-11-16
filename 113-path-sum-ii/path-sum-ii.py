# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result,path=[],[]

        def fun(node,total):
            
            if not node:
                return []

            path.append(node.val)
            total+= node.val

            if node.left is None and node.right is None:
                if total==targetSum:
                    result.append(path[:])

            
            else:
                fun(node.left, total)
                fun(node.right, total)

            path.pop()
        fun(root,0)
        return result
            

