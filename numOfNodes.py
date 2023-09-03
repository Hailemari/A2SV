from collections import defaultdict

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent):
            freq = defaultdict(int)
            
            freq[labels[node]] += 1

            for neighbor in graph[node]:
                if neighbor != parent:
                    neighborFreq = dfs(neighbor, node)
                    for char, count in neighborFreq.items():
                        freq[char] += count

            subTreeCounts[node] = freq
            return freq
        
        subTreeCounts = {}
        dfs(0, -1)

        result = [0] * n

        for i in range(n):
            result[i] = subTreeCounts[i][labels[i]]

        return result