class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0 
        self.res = None
        
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            
            if self.res is not None:  # Check if already found
                return
                
            self.count += 1
            if self.count == k:
                self.res = node.val
                return 
                
            inorder(node.right)
        
        inorder(root)
        return self.res