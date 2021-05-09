class Solution:
    n = m = c = ans = 0
    
    def dfs(self, i: int, j: int, grid: []):
        
        if grid[i][j] == 0:
            return

        grid[i][j]=0
        self.c+=1
          
        for k in range(self.m):
            print(i,k)
            self.dfs(i,k,grid)
        
        for k in range(self.n):
            self.dfs(k,j,grid)
            
    def countServers(self, grid: List[List[int]]):
        
        self.n=len(grid)
        self.m=len(grid[0])
        
        for i in range(self.n):
            for j in range(self.m):
                self.c=0
                self.dfs(i,j,grid)
                if self.c > 1:
                    self.ans+=self.c;
        return self.ans
