# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        
        def check(node: TreeNode, depth):
            
            
            if node is None:
                return None
            
            if node.left is None and node.right is None:
                return (node, depth)
            
            
            left = check(node.left, depth+1)
            right = check(node.right, depth+1)
            
            
            if left and right:
                if left[1] == right[1]:
                    return (node, left[1])
                elif left[1] > right[1]:
                    return left
                else:
                    return right
            else:
                if not left:
                    return right
                else:
                    return left
                
        
        result = check(root, 0)
        return result[0]
            
                
            
        
