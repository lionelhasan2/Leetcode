# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validateNode(root, lower_bound, upper_bound):
            if not root:
                return True
            if root.val > lower_bound and root.val < upper_bound:
                return validateNode(root.right,root.val,upper_bound) and validateNode(root.left,lower_bound, root.val)
            else:
                return False
        return validateNode(root,float("-inf"),float("inf"))