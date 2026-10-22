class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def count_ways(candies_to_distribute):
            if candies_to_distribute < 0:
                return 0
            return (candies_to_distribute + 2) * (candies_to_distribute + 1) // 2

        ans = count_ways(n)
        ans -= 3 * count_ways(n - (limit + 1))
        ans += 3 * count_ways(n - 2 * (limit + 1))
        ans -= count_ways(n - 3 * (limit + 1))

        return ans