class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        minHeap = [(matrix[i][0], i, 0) for i in range(n)]

        heapq.heapify(minHeap)

        count = 0
        while count < k:
            val, row, col = heapq.heappop(minHeap)
            count += 1
            if count == k:
                return val
            if col + 1 < n:
                heapq.heappush(minHeap, (matrix[row][col + 1], row, col + 1))
