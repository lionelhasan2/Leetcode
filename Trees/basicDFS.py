"""
Basic Depth-First Search (DFS) Algorithms
==========================================
DFS explores as far as possible along each branch before backtracking.
Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(h) where h is the height of the tree (recursion stack)
"""

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ===== DFS TRAVERSAL METHODS =====

# 1. PREORDER (Root -> Left -> Right)
def dfs_preorder_recursive(root):
    """
    Preorder: Visit root first, then left subtree, then right subtree
    Use case: Creating a copy of the tree, prefix expression evaluation
    """
    if not root:
        return []
    
    result = []
    result.append(root.val)  # Visit root
    result.extend(dfs_preorder_recursive(root.left))  # Visit left
    result.extend(dfs_preorder_recursive(root.right))  # Visit right
    return result



# 2. INORDER (Left -> Root -> Right)
def dfs_inorder_recursive(root):
    """
    Inorder: Visit left subtree, then root, then right subtree
    Use case: BST traversal (gives sorted order), expression tree evaluation
    """
    if not root:
        return []
    
    result = []
    result.extend(dfs_inorder_recursive(root.left))  # Visit left
    result.append(root.val)  # Visit root
    result.extend(dfs_inorder_recursive(root.right))  # Visit right
    return result



# 3. POSTORDER (Left -> Right -> Root)
def dfs_postorder_recursive(root):
    """
    Postorder: Visit left subtree, then right subtree, then root
    Use case: Deleting a tree, postfix expression evaluation
    """
    if not root:
        return []
    
    result = []
    result.extend(dfs_postorder_recursive(root.left))  # Visit left
    result.extend(dfs_postorder_recursive(root.right))  # Visit right
    result.append(root.val)  # Visit root
    return result



if __name__ == "__main__":
    # Create a sample tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("=== DFS Traversals ===")
    print(f"Preorder (recursive):  {dfs_preorder_recursive(root)}")
    print()
    print(f"Inorder (recursive):   {dfs_inorder_recursive(root)}")
    print()
    print(f"Postorder (recursive): {dfs_postorder_recursive(root)}")
    print()
