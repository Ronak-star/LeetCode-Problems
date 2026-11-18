class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)

        if k == 1:
            return n

        count = 0
        length = 1

        for i in range(1, n + k - 1):

            if colors[i % n] != colors[(i - 1) % n]:
                length += 1
            else:
                length = 1

            if length >= k:
                count += 1

        return count