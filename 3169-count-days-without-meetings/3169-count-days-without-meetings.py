class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        free_days = 0
        last_day = 0

        for start, end in meetings:
            if start > last_day:
                free_days += start - last_day - 1

            last_day = max(last_day, end)

        free_days += days - last_day

        return free_days