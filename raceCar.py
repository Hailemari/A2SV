class Solution:
    def racecar(self, target: int) -> int:
        queue = [(0, 1)] 
        visited = set([(0, 1)])
        steps = 0

        while queue:
            for _ in range(len(queue)):
                position, speed = queue.pop(0)

                if position == target:
                    return steps

                # Accelerate
                new_position = position + speed
                new_speed = speed * 2

                if (new_position, new_speed) not in visited and abs(new_position - target) < target:
                    visited.add((new_position, new_speed))
                    queue.append((new_position, new_speed))

                # Reverse
                new_speed = -1 if speed > 0 else 1

                if (position, new_speed) not in visited and abs(position - target) < target:
                    visited.add((position, new_speed))
                    queue.append((position, new_speed))

            steps += 1

        return -1