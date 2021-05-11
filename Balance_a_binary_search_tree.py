# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inOrder(node):
            return inOrder(node.left)+[node.val]+inOrder(node.right) if node else []
            
        def createTree(res):
            node = None
            if res:
                mid = len(res)//2
                node = TreeNode(res[mid])
                node.left = createTree(res[:mid])
                node.right = createTree(res[mid+1:])
            return node
        
        return createTree(inOrder(root))
        
