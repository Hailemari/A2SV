class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        queue = deque([(0, 0, 1)])

        while queue:
            row, col, pathLength = queue.popleft()
            if row == n - 1 and col == n - 1:
                return pathLength
            
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if 0 <= newRow < n and 0 <= newCol < n and grid[newRow][newCol] == 0:
                    queue.append((newRow, newCol, pathLength + 1))
                    grid[newRow][newCol] = 1 # make the cell as visited
        
        return -1 
