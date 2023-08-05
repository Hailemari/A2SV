class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = [-1, -1]
        firstOccurrence = self.search(nums, target, True)
        lastOccurrence = self.search(nums, target, False)

        answer[0] = firstOccurrence
        answer[1] = lastOccurrence 
        
        return answer
    def search(self, nums: List[int], target: int, isFirstOccurrence) -> List[int]:
        start, end = 0, len(nums) - 1
        ans = -1

        while start <= end:
            mid = (start + end) // 2

            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                ans = mid

                if isFirstOccurrence:
                    end = mid - 1
                else:
                    start = mid + 1
        
        return ans