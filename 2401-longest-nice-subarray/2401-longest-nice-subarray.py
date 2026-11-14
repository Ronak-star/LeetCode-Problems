class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        used = 0
        j = 0
        res = 0
        for i, num in enumerate(nums):
            while (used & num) != 0:
                used ^= nums[j]
                j += 1
            used |= num
            res = max(res, i- j + 1)
        return res