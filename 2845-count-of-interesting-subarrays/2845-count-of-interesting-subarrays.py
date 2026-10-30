class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        counts  = collections.defaultdict(int)
        counts[0] = 1

        current_prefix_count = 0
        result = 0

        for i in range(n):
            is_special = 1 if nums[i] % modulo == k  else 0
            current_prefix_count += is_special

            current_mod = current_prefix_count % modulo

            target_mod = (current_mod - k + modulo) % modulo

            result += counts[target_mod]

            counts[current_mod] += 1

        return result