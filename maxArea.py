class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxArea = 0
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0

            grid[i][j] = 0 # mark the cell as visited
            area = 1

              
            area += dfs(i - 1, j) 
            area += dfs(i + 1, j) 
            area += dfs(i, j - 1) 
            area += dfs(i, j + 1) 

            return area
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))

    
        return maxArea
                

                