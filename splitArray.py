class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        tails = defaultdict(int)

        for num in nums:
            freq[num] += 1

        for num in nums:
            if freq[num] == 0:
                continue

            freq[num] -= 1
            
            if tails[num - 1] > 0:
                tails[num - 1] -= 1
                tails[num] += 1
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                tails[num + 2] += 1
            else:
                return False
            
        return True