class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        count = [0] * (n + 1)

        for start, end in requests:
            count[start] += 1
            count[end + 1] -= 1
        
        for i in range(1, n):
            count[i] += count[i-1]
        
        count.sort(reverse=True)
        nums.sort(reverse=True)

        maxTotalSum = 0
        for i in range(n):
            maxTotalSum = (maxTotalSum + nums[i] * count[i]) % MOD
        
        return maxTotalSum
        