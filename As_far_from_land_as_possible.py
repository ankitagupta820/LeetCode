class Solution:
    def maxDistance(self, mat: List[List[int]]) -> int:
        
        Q = deque()
        n = len(mat)
        dist = [[math.inf for v in range(n)] for j in range(n)]
        result=-1
        
        
        def BFS(mat: List[List[int]]):
            
            nonlocal dist
            nonlocal result
            while Q:
                
                i,j = Q.popleft()
                nbrs = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]

                for x,y in nbrs:
                    if 0<=x<n and 0<=y<n:
                        if mat[x][y] == 1:
                            dist[x][y] = 0
                        elif dist[x][y] > dist[i][j]+1:
                            dist[x][y]=dist[i][j]+1
                            result = max(result,dist[x][y])
                            Q.append((x,y))
               
            
        for i in range(n):
            for j in range(n):
                if mat[i][j] == 1:
                    dist[i][j]=0
                    Q.append((i,j))
        
        BFS(mat)
        return result
        
