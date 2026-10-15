import heapq

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        max_day = 0
        for event in events:
            max_day = max(max_day, event[1])

        events.sort()

        pq = []  # min heap
        ans = 0
        i = 0
        n = len(events)

        for d in range(1, max_day + 1):
            while i < n and events[i][0] <= d:
                heapq.heappush(pq, events[i][1])
                i += 1

            while pq and pq[0] < d:
                heapq.heappop(pq)

            if pq:
                heapq.heappop(pq)
                ans += 1

        return ans