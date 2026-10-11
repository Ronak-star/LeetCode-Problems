class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_val = max(nums)

        ans = 0
        current_streak = 0

        for num in nums:
            if num == max_val:
                current_streak += 1
            else:
                current_streak = 0

            ans = max(ans, current_streak)

        return ans