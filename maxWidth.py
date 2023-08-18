# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxWidth = 0
        queue = [(root, 0)]

        while queue:
            levelLength = len(queue)
            _, firstPos = queue[0]

            for i in range(levelLength):
                node, pos = queue.pop(0)
                if node.left:
                    queue.append((node.left, 2 * (pos - firstPos)))
                if node.right:
                    queue.append((node.right, 2 * (pos - firstPos) + 1))

            maxWidth = max(maxWidth, pos - firstPos + 1)
        
        return maxWidth
                