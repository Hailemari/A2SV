# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root == None:
            return result
        if not root.left and not root.right:
            result.append([root.val])
            return result

        return self.helper([root], result)

    def helper(self, nodes, result):
        newNodes = []
        levelValues = []

        for node in nodes:
            levelValues.append(node.val)
            if node.left:
                newNodes.append(node.left)
            if node.right:
                newNodes.append(node.right)
        
        if levelValues:
            result.append(levelValues)

        if newNodes:
            return self.helper(newNodes, result)
        return result