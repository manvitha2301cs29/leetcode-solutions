# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        def help(n):
            if not n :
                return 
            l = n.left 
            r = n.right
            n.right = l 
            n.left = r 
            help(n.right)
            help(n.left)
        help(root)
        return root 
