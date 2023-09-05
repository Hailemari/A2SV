class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = {}
        
        for i in range(1,len(parent)):
            if parent[i] not in graph:
                graph[parent[i]]=[i]
            else:
                graph[parent[i]].append(i)
            
        self.ans = 1
        def dfs(i):
            if i not in graph:
                return 1
            res = 1
            for j in graph[i]:
                length = dfs(j)
                if s[i] != s[j]:
                    self.ans = max(self.ans, length + res)
                    res = max(res, length + 1)
            return res
        
        dfs(0)
        return self.ans