class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(x, y):
            if not (0 <= x < len(board)) or not (0 <= y < len(board[0])) or board[x][y] != 'E':
                return
            
            mines = countAdjacentMines(x, y)
            
            if mines == 0:
                board[x][y] = 'B'
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        dfs(x + dx, y + dy)
            else:
                board[x][y] = str(mines)
        
        def countAdjacentMines(x, y):
            mines = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 'M':
                        mines += 1
            return mines
        
        clickX, clickY = click
        
        if board[clickX][clickY] == 'M':
            board[clickX][clickY] = 'X'
        else:
            dfs(clickX, clickY)
        
        return board
