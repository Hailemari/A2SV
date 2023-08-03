class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengersTimeline = [0] * 1001

        for trip in trips:
            passengers, start, end = trip
            passengersTimeline[start] += passengers
            passengersTimeline[end] -= passengers

        currentPassengers = 0
        for passengersChange in passengersTimeline:
            currentPassengers += passengersChange

            if currentPassengers > capacity:
                return False
        
        return True