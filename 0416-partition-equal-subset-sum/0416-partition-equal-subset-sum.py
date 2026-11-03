class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2

        possible_sums = {0}

        for num in nums:
            sums_to_add = set()

            for s in possible_sums:
                new_sum = s + num
                if new_sum == target:
                    return True
                if new_sum  < target:
                    sums_to_add.add(new_sum)
            
            possible_sums.update(sums_to_add)

        return target in possible_sums