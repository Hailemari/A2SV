class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValidCapacity(middle):
            currentDay = 1
            currentLoad = 0

            for weight in weights:
                if currentLoad + weight > middle:
                    currentDay += 1
                    currentLoad = weight
                
                else:
                    currentLoad += weight
            
            return currentDay <= days
        
        minCapacity = max(weights)
        maxCapacity = sum(weights)

        while minCapacity <= maxCapacity:
            midCapacity = (minCapacity + maxCapacity) // 2

            if isValidCapacity(midCapacity):
                maxCapacity = midCapacity - 1
            else:
                minCapacity = midCapacity + 1
        
        return minCapacity