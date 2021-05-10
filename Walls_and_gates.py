class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
       
        def BFS(rooms):
            
            nonlocal Q
            while Q:
                i,j = Q.pop()
                nbrs = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]

                for x,y in nbrs:
                    if 0<=x<m and 0<=y<n and rooms[x][y] > 0 and rooms[x][y] >= rooms[i][j]+1:
                            rooms[x][y] = rooms[i][j]+1
                            Q.append((x,y))
                    
         
        Q = deque()
        m = len(rooms)
        n= len(rooms[0])
            
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    Q.append((i,j))
        
        BFS(rooms)
