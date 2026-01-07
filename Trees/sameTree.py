# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True # Both missing
        if not p or not q:
            return False # Only one missing
        # Compare whether vals at root are the same
        if p.val != q.val:
            return False
        else:
            return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right))
