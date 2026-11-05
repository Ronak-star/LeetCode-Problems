class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occurrence = {char: index for index, char in enumerate(s)}

        result = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])

            if i == end:
                partition_size = end - start + 1
                result.append(partition_size)
                start = i + 1

        return result