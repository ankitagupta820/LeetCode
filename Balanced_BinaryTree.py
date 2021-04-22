# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Balanced Binary Tree has the height difference of left and right subtree no more than 1.
"""

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def check(root: TreeNode)-> int:
            
            if root is None:
              return 0

            l = check(root.left)
            r = check(root.right)

            if l == -1 or r == -1 or  abs(l-r) > 1 :
              return -1
            else:
              return max(l,r)+1
        
        
        
        if check(root) == -1:
            return False
        else:
            return True
      
        
