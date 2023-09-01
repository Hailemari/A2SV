# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        def dfs(node):
            if not node:
                return ""
            
            leftStr = dfs(node.left)
            rightStr = dfs(node.right)

            result = str(node.val)

            if leftStr or rightStr:
                result += f"({leftStr})"
            
            if rightStr:
                result += f"({rightStr})"

            return result
        
        return dfs(root)
            
