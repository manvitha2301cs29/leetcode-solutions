# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ans = 0 

        def help(node):
            if not node :
                return 0 
            else :
                return max(help(node.right) , help(node.left)) + 1 
        return help(root)
        