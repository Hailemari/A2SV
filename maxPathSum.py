# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            leftMax = max(0, dfs(node.left))
            rightMax = max(0, dfs(node.right))

            currentMax = node.val + leftMax + rightMax

            self.maxSum = max(self.maxSum, currentMax)

            return node.val + max(leftMax, rightMax)

        self.maxSum = float('-inf')
        dfs(root)

        return self.maxSum