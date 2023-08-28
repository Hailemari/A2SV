n = int(input())
m = int(input())

# create an empty adjacency list
adjList = [[] for _ in range(n + 1)]

for _ in range(m):
    op, *args = map(int, input().split())
    if op == 1:
        u, v = args
        adjList[u].append(v)
        adjList[v].append(u)
    elif op == 2:
        u = args[0]
        print(" ".join(map(str, adjList[u])))