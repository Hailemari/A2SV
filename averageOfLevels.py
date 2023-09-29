# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            levelSum = 0
            levelCount = len(queue)

            for _ in range(levelCount):
                node = queue.popleft()
                levelSum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        
            result.append(levelSum / levelCount)

        return result