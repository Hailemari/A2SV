from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
        
        m, n = len(mat), len(mat[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()

        # Initialize the queue with the positions of all 0s and mark them as visited.
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                else:
                    mat[i][j] = -1 # mark non-zero cells as unvisited with -1

        while queue:
            row, col, distance = queue.popleft()
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc

                if 0 <= newRow < m and 0 <= newCol < n and mat[newRow][newCol] == -1:
                    mat[newRow][newCol] = distance + 1
                    queue.append((newRow, newCol, distance + 1))
        
        return mat

