class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        low = 1
        high = min(ranks) * cars * cars

        def check(time):
            total_repaired = 0
            for rank in ranks:
                total_repaired += int((time / rank) ** 0.5)
            return total_repaired >= cars

        while low < high:
            mid = (low + high) // 2

            if check(mid):
                high = mid
            else:
                low = mid + 1

        return low