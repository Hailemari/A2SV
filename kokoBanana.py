class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        while start < end:
            mid = (start + end) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours <= h:
                end = mid
            else:
                start = mid + 1
            
        return start

