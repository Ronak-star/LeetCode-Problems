from typing import List
import collections

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        total_distinct = len(set(nums))

        count = 0
        left = 0
        window_counts = collections.Counter()

        for right in range(n):
            window_counts[nums[right]] += 1

            while len(window_counts) == total_distinct:
                count += (n - right)

                window_counts[nums[left]] -= 1

                if window_counts[nums[left]] == 0:
                    del window_counts[nums[left]]

                left += 1

        return count