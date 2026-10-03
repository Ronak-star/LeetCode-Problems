class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)
        
        for i in range(1, n - 1):
            # Skip duplicate starting positions to avoid double counting plateaus
            if nums[i] == nums[i - 1]:
                continue
            
            # Find closest left non-equal neighbor
            left = 0
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    left = -1  # left neighbor is smaller
                    break
                elif nums[j] > nums[i]:
                    left = 1   # left neighbor is larger
                    break
            
            # Find closest right non-equal neighbor
            right = 0
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    right = -1  # right neighbor is smaller
                    break
                elif nums[j] > nums[i]:
                    right = 1   # right neighbor is larger
                    break
            
            # Hill: both left and right neighbors are smaller (-1, -1)
            # Valley: both left and right neighbors are larger (1, 1)
            if left != 0 and right != 0 and left == right:
                res += 1
                
        return res