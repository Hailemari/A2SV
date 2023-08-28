n = int(input())
adjMat = [list(map(int, input().split())) for _ in range(n)]
sources = []
sinks = []

for i in range(n):
    isSource = True
    isSink = True

    for j in range(n):
        if adjMat[j][i] == 1:
            isSource = False
        if adjMat[i][j] == 1:
            isSink = False
    
    if isSource:
        sources.append(i + 1)
    if isSink:
        sinks.append(i + 1)

print(len(sources), *sources)
print(len(sinks), *sinks)