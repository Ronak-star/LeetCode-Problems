class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_points = 0
        high_priority_pair = "ab"
        low_priority_pair = "ba"

        if x < y:
            x, y = y, x
            high_priority_pair, low_priority_pair = low_priority_pair, high_priority_pair

        
        stack = []
        for char in s:
            if char == high_priority_pair[1] and stack and stack[-1] == high_priority_pair[0]:

                stack.pop()
                total_points += x
            else:
                stack.append(char)

        new_stack = []
        for char in stack:
            if char == low_priority_pair[1] and new_stack and new_stack[-1] == low_priority_pair[0]:
                new_stack.pop()
                total_points += y
            else:
                new_stack.append(char)

        return total_points