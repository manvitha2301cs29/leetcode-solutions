# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def help(l,r):
            if (not l and r) or (not r and l) :
                return False 
            if  not l and not r :
                return True 
            if l.val != r.val :
                return False 
            return help(l.left , r.right) and help(l.right , r.left)
        if not root :
            return True 
        return help(root.left , root.right)
            