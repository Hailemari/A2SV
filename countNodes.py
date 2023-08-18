# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = 0

        def postOrder(node):
            nonlocal result

            if not node:
                return 0, 0
            
            leftSum, leftCount = postOrder(node.left)
            rightSum, rightCount = postOrder(node.right)

            sum = node.val + leftSum + rightSum
            count = 1 + leftCount + rightCount

            if sum // count == node.val:
                result += 1

            return sum, count

        postOrder(root)
        return result