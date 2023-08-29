def matToList(adjMat, n):
    count = 0
    vertices = []
    for i in range(n):
        for j in range(n):
            if adjMat[i][j] == 1:
                count += 1
                vertices.append(j + 1)
        print(count, *vertices)
        count = 0
        vertices.clear()
        


n = int(input())
adjMat = [list(map(int, input().split())) for _ in range(n)]
matToList(adjMat, n)

