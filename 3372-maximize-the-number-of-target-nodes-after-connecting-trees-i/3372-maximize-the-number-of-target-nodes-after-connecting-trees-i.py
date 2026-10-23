import collections

class Solution:
    def _dfs_recursive_worker(self, u_node: int, parent: int, adj: dict, k_val: int) -> int:
        if k_val < 0:
            return 0

        current_sum = 1

        for neighbor in adj[u_node]:
            if neighbor == parent:
                continue

            current_sum += self._dfs_recursive_worker(
                neighbor, u_node, adj, k_val - 1
            )

        return current_sum

    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]], k: int) -> list[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1

        adj1 = collections.defaultdict(list)
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)

        adj2 = collections.defaultdict(list)
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        max_contribution_from_tree2 = 0

        for j in range(m):
            count = self._dfs_recursive_worker(j, -1, adj2, k - 1)
            max_contribution_from_tree2 = max(
                max_contribution_from_tree2, count
            )

        results = []

        for i in range(n):
            count_from_tree1 = self._dfs_recursive_worker(i, -1, adj1, k)
            results.append(count_from_tree1 + max_contribution_from_tree2)

        return results