class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()

        ans = 1

        start_val = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - start_val > k:
                ans += 1
                start_val = nums[i]

        return ans