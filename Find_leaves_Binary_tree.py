# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution(object):
    
    def findLeaves(self, root):
        
        def order(root, dic):
            if not root:
                return 0
            
            left = order(root.left, dic)
            right = order(root.right, dic)
            
            lev = max(left, right) + 1
            dic[lev] += root.val,
            return lev
        
        
        dic, result = collections.defaultdict(list), []
        order(root, dic)
        
        for i in range(1, len(dic) + 1):
            result.append(dic[i])
        return result
