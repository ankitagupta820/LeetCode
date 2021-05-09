class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
"""
Check for two conditions:
1. The root value of left and right subtree are same.
2. Left subtree is mirror of right subtree. i.e recurse(left.left,right.right) and recurse(left.right, right.left)
"""
class Solution:
    
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def traverse(left: TreeNode, right:TreeNode)->bool:
            
            if not left and not right:
                return True
            
            if (not left and right) or (left and not right):
                return False
            
            return (left.val == right.val) and traverse(left.left, right.right) and traverse(left.right, right.left)
        
        return traverse(root.left, root.right)
        
