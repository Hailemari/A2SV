class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)

        tasks.sort(key = lambda x : x[0])
        result = []
        minHeap = []
        i = 0
        time = tasks[0][0]
        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, tasks[i][1:])
                i += 1

            if not minHeap:
                time = tasks[i][0]
            
            else:
                procTime, index = heapq.heappop(minHeap)
                result.append(index)
                time += procTime
        
        return result
