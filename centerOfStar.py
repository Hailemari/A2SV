class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first = edges[0][0]
        second = edges[0][1]
        isFirst = True
        for i in range(1, len(edges)):
            if first not in edges[i]:
                isFirst = False
                
        if isFirst:
            return first
        else:
            return second
