class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7


        powers = []
        for i in range(30):
            if (n >> i) & 1:
                powers.append(1 << i) 
        
        answers = []
        for left, right in queries:
            product = 1
            for i in range(left, right + 1):
                product = (product * powers[i]) % MOD
            answers.append(product)

        return answers