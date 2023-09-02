class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def isDetonated(bomb1, bomb2):
            return (bomb1[0] - bomb2[0])**2 + (bomb1[1] - bomb2[1])**2 <= bomb1[2] ** 2
        
        def dfs(bombs, start):
            detonated = 1
            for i in range(len(bombs)):
                if not visited[i] and isDetonated(bombs[start], bombs[i]):
                    visited[i] = True
                    detonated += dfs(bombs, i)
            
            return detonated
        
        maxDetonated = 0

        for i in range(len(bombs)):
            visited = [False] * len(bombs)
            visited[i] = True
            maxDetonated = max(maxDetonated, dfs(bombs, i))

        return maxDetonated