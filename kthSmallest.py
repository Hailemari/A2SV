# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = [0] * 2
        self.inorder(root, nums, k)

        return nums[1]

    def inorder(self, node, nums, k):
        if node == None:
            return
        
        self.inorder(node.left, nums, k)
        nums[0] += 1
        if(nums[0] == k):
            nums[1] = node.val
            return
        
        self.inorder(node.right, nums, k)