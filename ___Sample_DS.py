class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

        
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
