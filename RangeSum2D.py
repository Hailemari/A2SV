class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.cumulativeSum = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                self.cumulativeSum[i][j] = matrix[i-1][j-1] + self.cumulativeSum[i-1][j] + self.cumulativeSum[i][j-1] - self.cumulativeSum[i-1][j-1]

        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.cumulativeSum[row2+1][col2+1] - self.cumulativeSum[row1][col2+1] - self.cumulativeSum[row2+1][col1] + self.cumulativeSum[row1][col1]
        


