import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])

        min_arrival_time = [[float('inf')] * m for _ in range(n)]
        min_arrival_time[0][0] = 0

        pq = [(0, 0, 0)]

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while pq:
            time_curr_cell_arrival, r, c = heapq.heappop(pq)

            if time_curr_cell_arrival > min_arrival_time[r][c]:
                continue

            if r == n - 1 and c == m - 1:
                return time_curr_cell_arrival

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < n and 0 <= nc < m:
                    time_to_start_moving_to_neighbor = max(
                        time_curr_cell_arrival,
                        moveTime[nr][nc]
                    )

                    time_neighbor_arrival = (
                        time_to_start_moving_to_neighbor + 1
                    )

                    if time_neighbor_arrival < min_arrival_time[nr][nc]:
                        min_arrival_time[nr][nc] = time_neighbor_arrival

                        heapq.heappush(
                            pq,
                            (time_neighbor_arrival, nr, nc)
                        )

        return -1