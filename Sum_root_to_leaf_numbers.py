# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    
    sum = 0
    def DFS(self,node: TreeNode, path: str):
        
        
            if node is None:
                return
        
            if node.left is None and node.right is None:
                self.sum+= int(path+str(node.val))
                return
        
            path = path+str(node.val)
    
            self.DFS(node.left, path)
            self.DFS(node.right, path)
        
    def sumNumbers(self, root: TreeNode) -> int:
        
        if root is None:
            return []
        
        self.DFS(root, "")
        return self.sum
