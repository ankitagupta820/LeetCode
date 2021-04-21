"""
Find the size of Binary tree i.e number of total nodes in the tree
"""

class TreeNode:
    def __init__(self, val: int, left: TreeNode, right: TreeNode):
        self.val = val
        self.left = left
        self.right = right

            
# Inductive approach 
def size(root: TreeNode):
  
    if root is None:
        return 0  
    return size(root.left) + size(root.right) + 1

    
    
# Traverse and accumulate approach
def size(root: TreeNode):
    size = 0
    def getSize(node: TreeNode):
        # base case
        if node is None:
            return 0
        else:
            size+= getSize(node.left) + getSize(node.right) + 1
    
    getSize(root)
    return size;
        
