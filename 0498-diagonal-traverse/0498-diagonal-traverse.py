class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []
        
        M, N = len(mat), len(mat[0])

        diagonals = defaultdict(list)

        for i in range(M):
            for j in range(N):
                diagonals[i+j].append(mat[i][j])
        
        result = []

        for i in range(M + N - 1):
            if i % 2 == 0:
                diagonals[i].reverse()

            result.extend(diagonals[i])
        
        return result

        