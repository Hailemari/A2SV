class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalColor = image[sr][sc]

        if originalColor == color:
            return image
        
        def dfs(row, col):
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]):
                return
            
            if image[row][col] != originalColor:
                return

            image[row][col] = color
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        dfs(sr, sc)

        return image