class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = sorted(str(n))

        for i in range(30):
            power_of_2 = 1 << i

            p_s = sorted(str(power_of_2))

            if s == p_s:
                return True

        return False
        