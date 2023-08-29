def numRoads(adjMat, n):
    roads = 0
    for i in range(n):
        for j in range(n):
            if adjMat[i][j] == 1:
                roads += 1


    print(roads // 2)
n = int(input())
adjMat = [list(map(int, input().split())) for _ in range(n)]
numRoads(adjMat, n)