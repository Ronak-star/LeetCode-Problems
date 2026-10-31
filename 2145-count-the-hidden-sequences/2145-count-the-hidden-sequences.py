from itertools import accumulate

class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        prefix_sums = list(accumulate(differences, initial=0))

        sequence_range = max(prefix_sums) - min(prefix_sums)

        return max(0, (upper - lower) - sequence_range + 1)