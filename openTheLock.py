from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        queue = deque([("0000", 0)])

        while queue:
            currentLock, turns = queue.popleft()

            if currentLock == target:
                return turns
            
            if currentLock in visited or currentLock in deadends:
                continue

            visited.add(currentLock)
            for i in range(4):
                digit = int(currentLock[i])

                for diff in [-1, 1]:
                    newDigit = (digit + diff) % 10
                    newLock = currentLock[:i] + str(newDigit) + currentLock[i+1:]
                    if newLock not in visited:
                        queue.append((newLock, turns + 1))
        return -1