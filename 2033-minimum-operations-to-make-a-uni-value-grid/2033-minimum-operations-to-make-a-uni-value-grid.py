class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        m = len(grid)
        n = len(grid[0])

        nums = []

        for r in range(m):
            for c in range(n):
                nums.append(grid[r][c])

        remainder = nums[0] % x

        for num in nums:
            if num % x != remainder:
                return -1

        nums.sort()

        median = nums[len(nums) // 2]

        total_ops = 0

        for num in nums:
            total_ops += abs(num - median) // x

        return total_ops