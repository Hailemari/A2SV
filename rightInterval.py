from typing import List
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted([(s, i) for i, (s, e) in enumerate(intervals)])
        res = [-1] * len(intervals)

        for i, (s, e) in enumerate(intervals):
            idx = self.binarySearch(starts, e)
            if idx != len(starts):
                res[i] = starts[idx][1]
        
        return res 
    
    def binarySearch(self, arr, target):
        start, end = 0, len(arr)

        while start < end:
            mid = start + (end - start) // 2
            if arr[mid][0] < target:
                start = mid + 1
            else:
                end = mid
        
        return start
