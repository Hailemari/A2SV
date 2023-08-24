class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        result = []
        minHeap = []
        for i in range(min(len(nums1), k)):
            heapq.heappush(minHeap, (nums1[i] + nums2[0], i, 0))
        
        while k > 0 and minHeap:
            _, i, j = heapq.heappop(minHeap)
            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))
            
            k -= 1
        return result