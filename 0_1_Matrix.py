class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        
        Q = deque()
        m = len(mat)
        n = len(mat[0])
        dist = [[math.inf for v in range(n)] for j in range(m)]
        
        
        def BFS(mat: List[List[int]]):
            
            nonlocal dist
            while Q:
                
                i,j = Q.popleft()
                nbrs = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]

                for x,y in nbrs:
                    if 0<=x<m and 0<=y<n:
                        if mat[x][y] == 0:
                            dist[x][y] = 0
                        elif dist[x][y] > dist[i][j]+1:
                            dist[x][y]=dist[i][j]+1
                            Q.append((x,y))
               
            
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    dist[i][j]=0
                    Q.append((i,j))
        
        BFS(mat)
        return dist
 
