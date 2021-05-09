# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        def traverse(p: TreeNode, q: TreeNode):
            
            
            if not p and not q:
                return True
            
            if (not p and q) or (p and not q):
                return False
            
            if p.val == q.val:
                return traverse(p.left, q.left) and traverse(p.right, q.right)
            else: 
                return False
                
         
        return traverse(p, q)
