class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inDegrees = [0] * n
        for _, to in edges:
            inDegrees[to] += 1
        
        vertices = []
        for vertex in range(n):
            if inDegrees[vertex] == 0:
                vertices.append(vertex)

        return vertices