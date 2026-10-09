class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.0

        memo = {}

        def solve(a, b):
            if (a, b) in memo:
                return memo[(a, b)]

            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            
            prob = 0.25 * (solve(a - 100, b) + 
                           solve(a - 75, b - 25) +
                           solve(a - 50, b - 50) + 
                           solve(a - 25, b - 75))
            
            memo[(a, b)] = prob
            return prob

        return solve(n , n)