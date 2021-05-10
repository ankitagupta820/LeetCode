"""
    BFS of Tree.If child is None, then no more children should be found.
"""

def Solution(root: treeNode)->bool:
    from collections import deque
    
    if not root:
        return True
    
    bfs_q = deque([root])
    
    no_more_children = False
    while bfs_q:
        
        cur_node = bfs_q.popleft()
        
        if cur_node.left is None:
            no_more_children = True
            
        if cur_node.left:
            if no_more_children:
                return False
            
            bfs_q.append(cur_node.left)
        
        if cur_node.right is None:
            no_more_children = True
            
        if cur_node.right:
            if no_more_children:
                return False
            bfs_q.append(cur_node.right)
            
    return True




# def solution(root):
    
#     height = -1
#     completeness = False
#     lastLevel = []
    
# #     Finds the height of the Tree
#     def findHeight(node: TreeNode):
#         if node is None:
#             return 0
        
#         return max(findHeight(node.left), findHeight(node.right))+1
    
# #     Checks is all the null nodes are at the last level. Returns False if null node in middle of the Tree.

#     def checkComplete(node: TreeNode, level)->bool:
        
#         nonlocal height
        
#         # Collect all the nodes from left to right on the last level in lastlevel array.
#         if level == height:
#             if node is None:
#                 lastLevel.append(None)
#             else:
#                 lastLevel.append(node.val)
        
#         if node is None and level < height:
#             return False
        
#         if node is None:
#             return True
        
#         l = checkComplete(node.left, level+1)
#         r = checkComplete(node.right, level +1)
        
#         return l and r

# #      Checks the leftness of the Tree. i.e all the null nodes in the last level are towards the right end of lastlevel array
#     def leftness()->bool:
        
#         nonlocal lastLevel
#         print(lastLevel)
#         for index in range(len(lastLevel)-1):
#             if lastLevel[index] is None and lastLevel[index+1] is not None:
#                 return False
        
#         return True
           
#     height = findHeight(root)
#     completeness = checkComplete(root,1)
#     leftness = leftness()
    
#     return completeness and leftness
