class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        zero_count = 0
        left = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Window length is (right - left + 1), and since 1 element must be deleted,
            # the valid subarray size of 1s is (right - left + 1) - 1 = right - left.
            max_length = max(max_length, right - left)

        return max_length