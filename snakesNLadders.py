from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n

        flatBoard = [0]
        for i in range(n - 1, -1, -1):
            if (n - 1 - i) % 2 == 0:
                flatBoard.extend(board[i])
            else:
                flatBoard.extend(reversed(board[i]))
        
        queue = deque([(1, 0)])
        visited = set()
        visited.add(1)

        while queue:
            currSquare, moves = queue.popleft()

            if currSquare == target:
                return moves

            for i in range(1, 7):
                nextSquare = currSquare + i
                if nextSquare <= target:
                    nextSquare = flatBoard[nextSquare] if flatBoard[nextSquare] != -1 else nextSquare
                    if nextSquare not in visited:
                        visited.add(nextSquare)
                        queue.append((nextSquare, moves + 1))

        return -1 