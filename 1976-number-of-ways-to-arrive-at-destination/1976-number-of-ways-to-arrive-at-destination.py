import heapq

class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        MOD = 10**9 + 7

        graph = {i: [] for i in range(n)}

        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        dist = [float('inf')] * n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1

        pq = [(0, 0)]

        while pq:
            time, u = heapq.heappop(pq)

            if time > dist[u]:
                continue

            for v, time_uv in graph[u]:
                new_time = dist[u] + time_uv

                if new_time < dist[v]:
                    dist[v] = new_time
                    ways[v] = ways[u]

                    heapq.heappush(pq, (new_time, v))

                elif new_time == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1]