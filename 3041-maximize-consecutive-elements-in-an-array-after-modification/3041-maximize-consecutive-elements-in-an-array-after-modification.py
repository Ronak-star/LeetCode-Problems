class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()

        dp = {}
        ans = 0

        for num in nums:
            dp[num + 1] = max(dp.get(num + 1, 0), dp.get(num, 0) + 1)
            dp[num] = max(dp.get(num, 0), dp.get(num - 1, 0) + 1)

            ans = max(ans, dp[num], dp[num + 1])

        return ans