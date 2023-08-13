# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        path = ""

        if root == None:
            return paths
       
        self.dfs(root, path, paths)

        return paths
    def dfs(self, node, path, paths):
        path += str(node.val)
        
        if node.left == None and node.right == None:
            paths.append(path)
            return
        
        path += "->"
        if node.left != None:
            self.dfs(node.left, path, paths)

        if node.right != None:
            self.dfs(node.right, path, paths)
        