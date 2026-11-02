class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1_000_000_007
        
        def pow_mod(base, exp, modulus):
            res = 1
            base %= modulus
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % modulus
                base = (base * base) % modulus
                exp //= 2
            return res

        even_count = (n + 1) // 2
        odd_count = n // 2

        first_part = pow_mod(5, even_count, MOD)

        second_part = pow_mod(4, odd_count, MOD)
        
        return (first_part * second_part) % MOD