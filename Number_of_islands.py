class Solution:
    
    result = 0
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if len(grid) == 0:
            return self.result
        
        self.helper(grid)
        return self.result
        
     
    def DFS(self,grid, i,j):
        
        nr = len(grid)
        nc = len(grid[0])
        
        nbrs = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        
        grid[i][j] = 0
        for x, y in nbrs:
            if 0 <= x < nr and 0<= y < nc and grid[x][y] == "1":
                self.DFS(grid, x, y)
        
                  
    def helper(self, grid: List[List[str]]):
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    self.DFS(grid, i,j)
                    self.result += 1
