class Solution:
    
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = len(rooms)*[False]
            
        def DFS(visited: [], key: int):
            
            visited[key] = True
            
            for k in rooms[key]:
                if visited[k] == False:
                    DFS(visited, k)
        
        
        DFS(visited, 0)
        
        if not False in visited:
            return True
        else:
            return False
