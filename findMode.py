# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inOrderTraversal(node):
            nonlocal prevVal, currCount, maxCount, modes

            if not node:
                return
            
            inOrderTraversal(node.left)

            if node.val == prevVal:
                currCount += 1
            
            else:
                currCount = 1
            
            if currCount > maxCount:
                maxCount = currCount
                modes = [node.val]

            elif currCount == maxCount:
                modes.append(node.val)

            prevVal = node.val

            inOrderTraversal(node.right)

        prevVal = None
        currCount = 0
        maxCount = 0
        modes = []

        inOrderTraversal(root)
        return modes

