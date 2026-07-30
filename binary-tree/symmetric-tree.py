# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # edge case:
        if not root: 
            return True

        queue = deque()
        queue.append(root.left)
        queue.append(root.right)

        while queue:
            left = queue.popleft()
            right = queue.popleft()

            # Both null
            if not left and not right:
                continue

            # One Null
            if not left or not right:
                return False

            # value mismatch    
            if left.val != right.val:
                return False

            # Push the children in mirror order:
            queue.append(left.left)
            queue.append(right.right)

            queue.append(left.right)
            queue.append(right.left)

        return True
        