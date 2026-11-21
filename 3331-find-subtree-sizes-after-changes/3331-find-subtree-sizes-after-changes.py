class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Step 1: Build original tree
        orig_tree = [[] for _ in range(n)]

        for i in range(1, n):
            orig_tree[parent[i]].append(i)

        # Step 2: Find new parents
        new_parent = list(parent)
        last_seen = [-1] * 26

        def dfs1(node):
            char_idx = ord(s[node]) - ord('a')

            old_last = last_seen[char_idx]

            # Update parent if same character ancestor exists
            if old_last != -1:
                new_parent[node] = old_last

            last_seen[char_idx] = node

            for child in orig_tree[node]:
                dfs1(child)

            # Backtrack
            last_seen[char_idx] = old_last

        dfs1(0)

        # Step 3: Build new tree
        new_tree = [[] for _ in range(n)]

        for i in range(1, n):
            new_tree[new_parent[i]].append(i)

        # Step 4: Calculate subtree sizes
        ans = [0] * n

        def dfs2(node):
            size = 1

            for child in new_tree[node]:
                size += dfs2(child)

            ans[node] = size
            return size

        dfs2(0)

        return ans