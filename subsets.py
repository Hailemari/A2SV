class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(0, nums, [], result)
        return result
    def dfs(self, idx, nums, currSubset, result):
        result.append(currSubset[:])

        for i in range(idx, len(nums)):
            currSubset.append(nums[i])
            self.dfs(i+1, nums, currSubset, result)
            currSubset.pop()


