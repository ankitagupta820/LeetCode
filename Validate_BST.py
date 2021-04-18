# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
    """
    All Values in left subtree are smaller than root.
    All Values in right subtree are larger than root.
    """
        
        def recurse(cur_node: TreeNode, left= -math.inf, right = math.inf):
            
            if cur_node is None:
                return True
            
            if cur_node.val <= left or cur_node.val >= right:
                return False
            
            return recurse(cur_node.left, left, cur_node.val) and recurse(cur_node.right, cur_node.val, right)
        
        return recurse(root)
