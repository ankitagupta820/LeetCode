class Solution:
    
    
    def canReach(self, arr: List[int], start: int) -> bool:
        
        result:bool = False
        
        def DFS(arr: [], index: int):
            
            nonlocal result
            
            if arr[index] == -1:
                return
            
            elif arr[index] == 0:
                result = True
                return
            
            else:
                pos1 = index + arr[index]
                pos2 = index - arr[index]
                arr[index] = -1
                
                if  0 <= pos1 < len(arr):
                    DFS(arr, pos1)
                if 0<= pos2 <= len(arr):
                    DFS(arr,pos2)  
            
                
        DFS(arr, start)
        return result
        
