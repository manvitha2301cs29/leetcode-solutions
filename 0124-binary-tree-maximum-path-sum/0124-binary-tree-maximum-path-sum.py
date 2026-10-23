# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.maxi = -float('inf')

        def help(no):
            if not no :
                return 0 
            left = max(0,help(no.left)) if no.left else 0 
            right = max(0,help(no.right)) if no.right else 0 
            self.maxi = max(self.maxi , left + right + no.val)
            return max(left,right) + no.val 
        help(root)
        return self.maxi 