class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        counts = collections.Counter(nums)
        dominant_element = -1
        total_count = 0

        for element, count in counts.items():
            if count * 2 > n:
                dominant_element = element
                total_count = count
                break
            
        left_count = 0
        for i in range(n - 1):
            if nums[i] == dominant_element:
                left_count += 1

            right_count = total_count - left_count

            is_dominant_left = (left_count * 2) > (i + 1)
            is_dominant_right = (right_count * 2) > (n - 1 - i)

            if is_dominant_left and is_dominant_right:
                return i
                
        return -1