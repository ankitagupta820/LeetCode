import math
"""
Given a BST with non-negative values, find the minimum absolute difference between values of any two nodes.

"""
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
    
def findMinimumDiff(root: TreeNode)-> int:
  
  minimumDiff = math.inf
  def recurse(root: TreeNode):
    
    nonlocal minimumDiff
    
    if root is None:
      return -math.inf
      
    l = recurse(root.left)
    r = recurse(root.right)
    
    minimumDiff = min(minimumDiff, min(abs(root.val - l), abs(root.val-r)))
    return root.val
  
  recurse(root)
  return minimumDiff 
