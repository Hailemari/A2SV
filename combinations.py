class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def backtrack(start = 1, currCombination = []):
            if len(currCombination) == k:
                results.append(currCombination.copy())
                return
            
            for num in range(start, n+1):
                currCombination.append(num)
                backtrack(num+1, currCombination)
                currCombination.pop()
        
        backtrack()
        return results