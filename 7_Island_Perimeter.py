class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.peri = 0
        row = len(grid)
        col = len(grid[0])
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] != 1:
                        self.peri += 1
                    if j == 0 or grid[i][j-1] != 1:
                        self.peri += 1
                    if j == col-1 or grid[i][j+1] != 1:
                        self.peri += 1
                    if i == row-1 or grid[i+1][j] != 1:
                        self.peri += 1
                    
        return self.peri