class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:

        def can_allocate(mid):
            count = 0

            for candy in candies:
                count += candy // mid

            return count >= k

        left, right = 1, max(candies)
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if can_allocate(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer