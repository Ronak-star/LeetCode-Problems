class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        height = [0] * n

        for i in range(m):
            for j in range(n):
                height[j] = height[j] + 1 if mat[i][j] == 1 else 0

            for j in range(n):
                if height[j] > 0:
                    min_h = height[j]
                    for k in range(j, -1, -1):
                        min_h = min(min_h, height[k])
                        if min_h == 0:
                            break
                        res += min_h
     
        return res

        