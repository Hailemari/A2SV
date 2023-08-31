class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = 0
        visited = set()

        def dfs(city):
            visited.add(city)
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)
        
        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)

        return provinces