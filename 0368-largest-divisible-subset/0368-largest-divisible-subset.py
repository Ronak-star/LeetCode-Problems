class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)

        dp = [1] * n
        parent = [-1] * n

        max_size = 1
        max_idx = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if 1 + dp[j] > dp[i]:
                        dp[i] = 1 + dp[j]
                        parent[i] = j

            if dp[i] > max_size:
                max_size = dp[i]
                max_idx = i

        result = []
        curr_idx = max_idx

        while curr_idx != -1:
            result.append(nums[curr_idx])
            curr_idx = parent[curr_idx]

        return result[::-1]