# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        
        
        def same(node, subnode):


            if not node and not subnode:
                return True
            if not node or not subnode:
                return False
            if node.val !=subnode.val:
                return False
            return same(node.left,subnode.left) and same(node.right, subnode.right)

        if not root:
            return False

        if same(root,subRoot):
            return True
        

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)