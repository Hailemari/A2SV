class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # Create an adjacency list to represent the graph
        graph = defaultdict(list)
        print(graph)

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        # initialize a dictionary to store the group of each person (1 or -1)
        groups = {}

        def dfs(node, group):
            if node in groups:
                return groups[node] == group
            groups[node] = group
            for neighbor in graph[node]:
                if not dfs(neighbor, -group):
                    return False
            
            return True

        # Iterate through all people and group them, starting from ungrouped people
        for i in range(1, n + 1):
            if i not in groups and not dfs(i, 1):
                return False
        
        return True




        