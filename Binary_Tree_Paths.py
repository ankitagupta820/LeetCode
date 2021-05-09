
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    result = set()
    
    def DFS(self, node: TreeNode, path: str):
        
        
        if node is None:
            return
        
        if node.left is None and node.right is None:
            self.result.add(path+str(node.val))
            return
        
        path = path+str(node.val)+'->'
    
        self.DFS(node.left, path)
        self.DFS(node.right, path)
        
        
        
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        if root is None:
            return []
        
        self.result = set()
        self.DFS(root, "")
        return list(self.result)
