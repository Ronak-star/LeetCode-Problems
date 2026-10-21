class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)

            if root_i < root_j:
                parent[root_j] = root_i
            elif root_j < root_i:
                parent[root_i] = root_j
        
        for k in range(len(s1)):
            char1_val = ord(s1[k]) - ord('a')
            char2_val = ord(s2[k]) - ord('a')
            union(char1_val, char2_val)
        
        result_chars = []
        for char_base in baseStr:
            char_val = ord(char_base) - ord('a')
            root_val = find(char_val)
            result_chars.append(chr(root_val + ord('a')))
        
        return "".join(result_chars)