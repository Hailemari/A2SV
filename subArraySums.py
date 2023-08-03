from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        remaindersCount = defaultdict(int)
        remaindersCount[0] = 1

        runningSum = 0
        for n in nums:
            runningSum += n
            remainder = runningSum % k
            count += remaindersCount[remainder]
            remaindersCount[remainder] += 1

        return count

