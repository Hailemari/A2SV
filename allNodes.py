from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {}

        def buildGraph(node, parent):
            if node:
                if node not in graph:
                    graph[node] = []
                if parent:
                    graph[node].append(parent)
                    graph[parent].append(node)
                buildGraph(node.left, node)
                buildGraph(node.right, node)
        
        buildGraph(root, None)

        visited = set()
        queue = deque([(target, 0)])
        result = []

        while queue:
            node, distance = queue.popleft()
            visited.add(node)

            if distance == k:
                result.append(node.val)

            elif distance < k:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, distance + 1))

        return result