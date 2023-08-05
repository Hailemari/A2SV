class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] > arr[mid - 1]:
                start = mid
            else:
                end = mid