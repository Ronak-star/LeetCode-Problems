
from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])

        min_arrival_times = [
            [[float('inf')] * 2 for _ in range(m)]
            for _ in range(n)
        ]

        pq = [(0, 0, 0, 0)]
        min_arrival_times[0][0][0] = 0

        while pq:
            time_arr_curr, r, c, k_moves = heapq.heappop(pq)

            if time_arr_curr > min_arrival_times[r][c][k_moves % 2]:
                continue

            if r == n - 1 and c == m - 1:
                return time_arr_curr

            cost_for_next_move = 1 if k_moves % 2 == 0 else 2

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m:
                    time_to_initiate_move = max(
                        time_arr_curr, moveTime[nr][nc]
                    )

                    time_arr_neighbor = (
                        time_to_initiate_move + cost_for_next_move
                    )

                    next_k_moves = k_moves + 1

                    if time_arr_neighbor < min_arrival_times[nr][nc][next_k_moves % 2]:
                        min_arrival_times[nr][nc][next_k_moves % 2] = time_arr_neighbor

                        heapq.heappush(
                            pq,
                            (time_arr_neighbor, nr, nc, next_k_moves)
                        )

        return -1


