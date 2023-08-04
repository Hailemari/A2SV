# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        
        start, end = 1, n
        mid = (start + end) // 2
        
        while(start < end):
            if isBadVersion(mid):
                end = mid
                mid = (start + end) // 2
            else:
                start = mid + 1
                mid = (start + end) // 2
            
        return mid
        


        