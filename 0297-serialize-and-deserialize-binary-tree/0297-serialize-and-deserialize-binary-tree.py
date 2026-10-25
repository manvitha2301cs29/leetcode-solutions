# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = []
        if not root :
            return "#"
        q = deque()
        q.append(root)
        while q :
            
            
            n = q.popleft()
            if not n :
                s.append("#")
                continue
            s.append(str(n.val))
            
            q.append(n.left)
            
            q.append(n.right)
        return ",".join(s)

            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        idx = 0 
        if data == "#":
            return None
        
        d = data.split(",")
        root = TreeNode(int(d[0]))
        q = deque()
        q.append(root)
        i = 1 
        while q :
            n = q.popleft()
            if d[i] != "#":
                n.left = TreeNode(int(d[i]))
                q.append(n.left)
            i += 1 
            if d[i] !=  "#":
                n.right = TreeNode(int(d[i]))
                q.append(n.right)
            i += 1 
        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))