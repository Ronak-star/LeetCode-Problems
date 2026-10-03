class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []

        triangle = [[1]]

        for i in range(numRows - 1):
            prev_row = triangle[-1]
            new_row = [1]

            for j in range (len(prev_row) - 1):
                new_row.append(prev_row[j] + prev_row[j + 1])

            new_row.append(1)
            triangle.append(new_row)
        
        return triangle
        