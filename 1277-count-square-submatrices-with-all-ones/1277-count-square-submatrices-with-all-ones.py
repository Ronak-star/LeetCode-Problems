class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        ans = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    if r > 0 and c > 0:
                        matrix[r][c] = 1 + min(matrix[r-1][c], matrix[r][c-1], matrix[r-1][c-1])
                    ans += matrix[r][c]
        
        return ans
        