from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = ((1, 2, 3), (4, 5, 0))
        board = tuple(tuple(row) for row in board)

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque([(board, 0)])
        visited = set()

        while queue:
            currentBoard, depth = queue.popleft()

            if currentBoard == target:
                return depth
            
            # Find the position of the empty square (0)
            for i in range(2):
                for j in range(3):
                    if currentBoard[i][j] == 0:
                        x, y = i, j

            for dx, dy in moves:
                newX, newY = x + dx, y + dy

                # Check if the new position is within the board boundaries
                if 0 <= newX < 2 and 0 <= newY < 3:
                    # Create a new board configuration by swapping the empty square and the adjacent number
                    newBoard = [list(row) for row in currentBoard]
                    newBoard[x][y], newBoard[newX][newY] = newBoard[newX][newY], newBoard[x][y]
                    newBoard = tuple(tuple(row) for row in newBoard)

                    if newBoard not in visited:
                        queue.append((newBoard, depth + 1))
                        visited.add(newBoard)

        return -1

