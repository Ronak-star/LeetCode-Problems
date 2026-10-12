class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pos = [-1] * 32
        ans = [0] * n
        
        for i in range(n - 1, -1, -1):
            j = i
            for bit in range(32):
                if nums[i] & (1 << bit):
                    pos[bit] = i
                if pos[bit] != -1:
                    j = max(j, pos[bit])
            ans[i] = j - i + 1
            
        return ans