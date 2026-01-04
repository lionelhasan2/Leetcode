"""
Basic Breadth-First Search (BFS) Algorithms
============================================
BFS explores all nodes at the current level before moving to the next level.
Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(w) where w is the maximum width of the tree
"""

from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ===== BFS TRAVERSAL METHODS =====

def bfs_level_order(root):
    """
    Basic BFS traversal - visits nodes level by level
    Returns a flat list of all node values
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        # Add children to queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result



# ===== EXAMPLE USAGE =====

if __name__ == "__main__":
    # Create a sample tree:
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    
    print("=== BFS Traversals ===")
    print(f"Level order (flat):     {bfs_level_order(root)}")
    print()
    

    
    # Create symmetric tree for testing
    #       1
    #      / \
    #     2   2
    #    / \ / \
    #   3  4 4  3
    sym_root = TreeNode(1)
    sym_root.left = TreeNode(2)
    sym_root.right = TreeNode(2)
    sym_root.left.left = TreeNode(3)
    sym_root.left.right = TreeNode(4)
    sym_root.right.left = TreeNode(4)
    sym_root.right.right = TreeNode(3)
