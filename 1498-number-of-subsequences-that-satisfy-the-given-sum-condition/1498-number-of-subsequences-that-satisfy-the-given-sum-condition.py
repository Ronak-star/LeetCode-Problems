class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()

        powers = [1] * n
        for i in range(1, n):
            powers[i] = (powers[i - 1] * 2) % MOD

        res = 0
        left, right = 0, n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                count = powers[right - left]
                res = (res + count) % MOD
                left += 1
            else:
                right -= 1

        return res