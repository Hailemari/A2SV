from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Create a dictionary to map each bus stop to the list of bus routes that stop there
        stopToRoutes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stopToRoutes[stop].append(i)

        # Initialize a queue for BFS
        queue = deque([(source, 0)])  # (bus stop, number of buses taken)
        visitedStops = set()  # Set to keep track of visited bus stops
        visitedRoutes = set()  # Set to keep track of visited bus routes

        while queue:
            stop, busesTaken = queue.popleft()

            if stop == target:
                return busesTaken
            
            for routeIdx in stopToRoutes[stop]:
                if routeIdx not in visitedRoutes:
                    visitedRoutes.add(routeIdx)
                    for nextStop in routes[routeIdx]:
                        if nextStop not in visitedStops:
                            visitedStops.add(nextStop)
                            queue.append((nextStop, busesTaken + 1))
            
        return -1

        