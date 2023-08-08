class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]) -> int:
        self.leader = []
        self.times = times
        count = {}
        currentLeader = -1

        for i in range(len(persons)):
            person = persons[i]
            count[person] = count.get(person, 0) + 1

            if count[person] >= count.get(currentLeader, 0):
                currentLeader = person

            self.leader.append(currentLeader)

    def q(self, t: int) -> int:
        start, end = 0, len(self.times) - 1

        while start < end:
            mid = (start + end + 1) // 2

            if self.times[mid] <= t:
                start = mid
            else:
                end = mid - 1
        
        return self.leader[start]


