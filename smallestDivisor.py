class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        divisor = [ i for i in range(1, max(nums) + 1)]

        answer = 1
        start = 0
        end = len(divisor) - 1
        while start <= end:
            mid = (start + end) // 2
            
            sum = 0
            for num in nums:
                sum += math.ceil(num / divisor[mid])
            
            if sum > threshold:
                start = mid + 1
            else:
                end = mid - 1

        answer = divisor[start]

        return answer
        