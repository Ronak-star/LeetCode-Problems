
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        delta_array = [0] * (n + 1)

        for query in queries:
            left_val = query[0]
            right_val = query[1]

            delta_array[left_val] += 1
            delta_array[right_val + 1] -= 1

        current_operations = 0

        for i in range(n):
            current_operations += delta_array[i]

            if current_operations < nums[i]:
                return False

        return True

