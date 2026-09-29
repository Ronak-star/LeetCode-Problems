from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        # Sort diagonals starting from the first column
        # in descending order
        for i in range(n):
            tmp = [grid[i + j][j] for j in range(n - i)]
            tmp.sort(reverse=True)

            for j in range(n - i):
                grid[i + j][j] = tmp[j]

        # Sort diagonals starting from the first row
        # in ascending order
        for i in range(1, n):
            tmp = [grid[j][i + j] for j in range(n - i)]
            tmp.sort()

            for j in range(n - i):
                grid[j][i + j] = tmp[j]

        return grid