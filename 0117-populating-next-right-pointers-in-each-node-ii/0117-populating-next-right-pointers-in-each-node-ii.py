from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = deque([root])

        while q:
            l = len(q)
            prev = None

            for _ in range(l):
                curr = q.popleft()

                if prev:
                    prev.next = curr

                prev = curr

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            prev.next = None

        return root