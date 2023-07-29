class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(1, len(self.nums)):
            self.nums[i] = self.nums[i-1] + self.nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        
        return self.nums[right] - self.nums[left - 1]