class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        count = 0

        def dfs(node, component_nodes):
            visited[node] = True
            component_nodes.append(node)

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component_nodes)

        for i in range(n):
            if not visited[i]:
                component_nodes = []
                dfs(i, component_nodes)

                num_nodes = len(component_nodes)
                is_complete = True

                for u in component_nodes:
                    for v in component_nodes:
                        if u != v and v not in graph[u]:
                            is_complete = False
                            break

                    if not is_complete:
                        break

                if is_complete:
                    count += 1

        return count