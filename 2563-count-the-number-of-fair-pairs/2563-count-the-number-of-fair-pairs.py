from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)

        def count_less_equal(target):
            pair_count = 0
            left = 0
            right = n - 1

            while left < right:
                if nums[left] + nums[right] <= target:
                    pair_count += right - left
                    left += 1
                else:
                    right -= 1

            return pair_count

        count = count_less_equal(upper) - count_less_equal(lower - 1)

        return count