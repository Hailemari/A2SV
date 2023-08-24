class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = [-pile for pile in piles]
        heapq.heapify(maxHeap)

        for _ in range(k):
            mostStones = -heapq.heappop(maxHeap)
            newPile = mostStones - (mostStones // 2)
            heapq.heappush(maxHeap, -newPile)

        return -sum(maxHeap)