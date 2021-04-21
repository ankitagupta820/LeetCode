"""
Tilt is defined as: for all nodes SUM(abs (Left subtree node sum - Right subtree node sum))
Combine Inductive and accumulative approach. 
Inductive: to return sum of subtree.
Accumulative: for sum of absolute diff for each node.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    
    total = 0
    def findTilt(self, root: TreeNode) -> int:
        
        
        def tilt(node: TreeNode):

            if node is None:
                return 0

            left = tilt(node.left)
            right = tilt(node.right)

            diff = abs(left-right)
            self.total += diff
            return left+right+node.val

        tilt(root)
        return self.total
