class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(u, x):
            result = (hasApple[u], 0)
            for v in graph[u]:
                if v == x:
                    continue
                apple, cost = dfs(v, u)
                if apple:
                    result = (True, result[1] + cost + 2)
            
            return result

        return dfs(0, -1)[1]