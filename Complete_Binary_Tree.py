def solution(root):
    
    height = -1
    completeness = False
    lastLevel = []
    
#     Finds the height of the Tree
    def findHeight(node: TreeNode):
        if node is None:
            return 0
        
        return max(findHeight(node.left), findHeight(node.right))+1
    
#     Checks is all the null nodes are at the last level. Returns False if null node in middle of the Tree.

    def checkComplete(node: TreeNode, level)->bool:
        
        nonlocal height
        
        # Collect all the nodes from left to right on the last level in lastlevel array.
        if level == height:
            if node is None:
                lastLevel.append(None)
            else:
                lastLevel.append(node.val)
        
        if node is None and level < height:
            return False
        
        if node is None:
            return True
        
        l = checkComplete(node.left, level+1)
        r = checkComplete(node.right, level +1)
        
        return l and r

#      Checks the leftness of the Tree. i.e all the null nodes in the last level are towards the right end of lastlevel array
    def leftness()->bool:
        
        nonlocal lastLevel
        print(lastLevel)
        for index in range(len(lastLevel)-1):
            if lastLevel[index] is None and lastLevel[index+1] is not None:
                return False
        
        return True
           
    height = findHeight(root)
    completeness = checkComplete(root,1)
    leftness = leftness()
    
    return completeness and leftness
