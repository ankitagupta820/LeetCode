import math

"""
Find the maximum value in a Binary Tree.
"""

class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# induction solution
def findMaximum(root: TreeNode):
    
    if root is None:
        return -math.inf
    
    return max(root.val, max(findMaximum(root.left), findMaximum(root.right)))

# traverse and accumulate solution
def findMaximum(node:TreeNode):
    
    maximumVal = -math.inf
    def find(node: TreeNode):
        nonlocal maximumVal
        if node is None:
            return    
        maximumVal = max(node.val, max(findMaximum(node.left), findMaximum(node.right)))
    
    find(node)
    return maximumVal
