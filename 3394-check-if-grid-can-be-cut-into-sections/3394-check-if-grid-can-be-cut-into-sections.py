class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:

        def check(intervals):
            intervals.sort()

            sections = 0
            end = -1

            for start, finish in intervals:

                if start >= end:
                    sections += 1

                end = max(end, finish)

            return sections >= 3

        x_intervals = []
        y_intervals = []

        for sx, sy, ex, ey in rectangles:
            x_intervals.append([sx, ex])
            y_intervals.append([sy, ey])

        return check(x_intervals) or check(y_intervals)