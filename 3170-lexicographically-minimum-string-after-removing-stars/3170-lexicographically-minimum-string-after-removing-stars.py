class Solution:
    def clearStars(self, s: str) -> str:
        char_indices = [[] for _ in range(26)]

        removed_indices = set()

        for i, char in enumerate(s):
            if char == '*':
                removed_indices.add(i)
                for j in range(26):
                    if char_indices[j]:
                        removed_index = char_indices[j].pop()
                        removed_indices.add(removed_index)
                        break
            
            else:
                idx = ord(char) - ord('a')
                char_indices[idx].append(i)

        result = []
        for i, char in enumerate(s):
            if i not in removed_indices:
                result.append(char)

        return "".join(result)