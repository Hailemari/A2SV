# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

            def dfs(node, row, col):
                if not node:
                    return
                if col in columnMap:
                    columnMap[col].append((row, node.val))
                else:
                    columnMap[col] = [(row, node.val)]
                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)
            
            columnMap = {}
            
            dfs(root, 0, 0)
            result = []

            for col in sorted(columnMap.keys()):
                result.append([val for _, val in sorted(columnMap[col])])
            
            return result
