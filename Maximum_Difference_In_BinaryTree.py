import math
"""
Find the maximum difference between any two nodes of Tree
Hint: find the maximum and minimum elements
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


         
def maximumDiff(root: TreeNode):
    
    maximum = -math.inf
    minimum = math.inf
    
    def find(node: TreeNode):
        nonlocal maximum
        nonlocal minimum
        
        if node is None:
            return 
        
        minimum = min(minimum, node.val)
        maximum = max(maximum, node.val)
        
        find(node.left)
        find(node.right)
        
    find(root)
    return maximum-minimum

    
    
# Binary Tree
root = TreeNode(1)
t1 = TreeNode(3)
t2 = TreeNode(51)
root.left = t1
root.right = t2
t3 = TreeNode(6)
t4 = TreeNode(7)
t2.left = t3
t2.right = t4
t5 = TreeNode(50)
t1.left = t5

print(maximumDiff(root))
