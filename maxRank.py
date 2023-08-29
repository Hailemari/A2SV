class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adjMat = [[0] * n for _ in range(n)]
        maxRank = 0

        for ai, bi in roads:
            adjMat[ai][bi] += 1
            adjMat[bi][ai] += 1
        
        for i in range(n):
            for j in range(i + 1, n):
                rank = sum(adjMat[i]) + sum(adjMat[j]) - adjMat[i][j]
                maxRank = max(maxRank, rank)

        return maxRank
