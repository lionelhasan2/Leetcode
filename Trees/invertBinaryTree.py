# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        # Process left node
        left_node = root.left
        self.invertTree(left_node)

        # Process right node
        right_node = root.right
        self.invertTree(right_node)

        # Swap nodes
        root.left = right_node
        root.right = left_node

        return root
    
    #[2,1,3]
    # [4,2,7,1,3,6,9]