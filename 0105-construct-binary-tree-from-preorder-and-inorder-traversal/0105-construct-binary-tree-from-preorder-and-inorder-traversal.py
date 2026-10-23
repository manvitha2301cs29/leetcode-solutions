# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        n = len(preorder)
        # i keeps track of current index of preorder list 
        pre_i = 0 
        dic = defaultdict(int)
        for i,ni in enumerate(inorder):
            dic[ni] = i
        def help(left,right):
            if left > right :
                return 
            nonlocal pre_i 
            rv = preorder[pre_i]
            r = TreeNode(rv)
            pre_i += 1 
            r.left = help(left , dic[rv] - 1 )
            r.right = help(dic[rv] + 1 , right)
            return r 
        return help(0,n-1)
        