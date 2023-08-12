class Solution:
    def splitString(self, s: str) -> bool:
        result = []

        def backtrack(startIndex):
            if startIndex == len(s):
                if len(result) >= 2:
                    return True
                return False

            for i in range(startIndex, len(s)):
                result.append(int(s[startIndex:i+1]))
                if len(result) < 2 or result[-2] - result[-1] == 1:
                    if backtrack(i+1):
                        return True 
                
                result.pop()

            return False
        
        return backtrack(0)