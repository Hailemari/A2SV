def numOfTeams():
    a, b = map(int, input().split())
    print(min(min(a, b), (a + b) // 4))


testCases = int(input())
for _ in range(testCases):
    numOfTeams()