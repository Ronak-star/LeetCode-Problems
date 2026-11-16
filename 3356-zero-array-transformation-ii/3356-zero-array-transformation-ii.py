class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        n = len(nums)

        def check(k):
            diff = [0] * (n + 1)

            for i in range(k):
                l, r, val = queries[i]

                diff[l] += val
                diff[r + 1] -= val

            total = 0

            for i in range(n):
                total += diff[i]

                if nums[i] > total:
                    return False

            return True

        left, right = 0, len(queries)
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer