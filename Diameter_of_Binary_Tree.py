class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  

class Solution:
    """
    Biggest diameter is longest path in left subtree + longest path in right subtree.
    Combines induction and accumulate templates. 
    Uses induction for longest path, uses accumulation for longest diameter
    """
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        diameter = 0
        def recurse(cur_node: TreeNode)-> int:
            if not cur_node:
                return 0
            
            nonlocal diameter
            l = recurse(cur_node.left)
            r = recurse(cur_node.right)
            
            diameter = max(diameter, l+r)             
            return max(l, r) + 1
        
        recurse(root)
        return diameter
