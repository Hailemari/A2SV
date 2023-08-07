class Solution:
    def hIndex(self, citations: List[int]) -> int:
        start, end = 0, len(citations) - 1


        while start <= end:
            mid = start + (end - start) // 2
            
            if citations[mid] == len(citations) - mid:
                return citations[mid]
            elif citations[mid] > len(citations) - mid:
                end = mid - 1
            else:
                start = mid + 1

        return len(citations) - start


