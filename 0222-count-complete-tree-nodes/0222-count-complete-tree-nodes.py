# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        ans = 0 

        def height(node):
            if not node :
                return 0 
            return 1 + max(height(node.left), height(node.right))
        def help(node):
            if not node :
                return 0 
            lh = height(node.left)
            rh = height(node.right)
            if lh == rh :
                return (1<<lh) + help(node.right) 
            else :
                return (1<<rh)  + help(node.left)
        return help(root)
