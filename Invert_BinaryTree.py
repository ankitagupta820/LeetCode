"""
Invert Binary Tree i.e mirror image of tree. 
Hint: Flip the left and right nodes of each node.
"""

class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root is None:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right , left
        return root
