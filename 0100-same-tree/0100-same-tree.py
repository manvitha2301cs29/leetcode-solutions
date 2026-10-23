# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def help(np,nq):
            if (not np and nq ) or (np and not nq) :
                return False 
            elif (not np) and (not nq) :
                return True 
            elif nq.val != np.val :
                return False 
            else :
                return help(np.left , nq.left) and help(np.right , nq.right)
        return help(p,q)
            