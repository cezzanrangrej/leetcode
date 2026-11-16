# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):

        def getNodes(root):
            ans = []

            def dfs(node):
                if node is None:
                    ans.append(None)
                    return

                ans.append(node.val)
                dfs(node.left)
                dfs(node.right)

            dfs(root)
            return ans

        def getNodes1(root):
            ans = []

            def dfs(node):
                if node is None:
                    ans.append(None)
                    return

                ans.append(node.val)
                dfs(node.right)
                dfs(node.left)

            dfs(root)
            return ans

        rl = getNodes(root.left)
        rr = getNodes1(root.right)

        return rl == rr