def is_bicolourable(graph, n):
    color = [-1] * n
    color[0] = 0  # Start with color 0 for the first node

    stack = [0]

    while stack:
        node = stack.pop()

        for neighbor in graph[node]:
            if color[neighbor] == -1:
                color[neighbor] = 1 - color[node]
                stack.append(neighbor)
            elif color[neighbor] == color[node]:
                return False  # If adjacent nodes have the same color, it's not bipartite

    return True  # If all nodes can be coloured without conflicts, it's bipartite

while True:
    n = int(input())
    if n == 0:
        break

    l = int(input())
    graph = [[] for _ in range(n)]

    for _ in range(l):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    if is_bicolourable(graph, n):
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")