from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n
        prev = [-1] * n

        max_len = 1
        end_idx = 0

        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    dist = sum(a != b for a, b in zip(words[i], words[j]))

                    if dist == 1 and dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                end_idx = i

        result = []
        curr = end_idx

        while curr != -1:
            result.append(words[curr])
            curr = prev[curr]

        return result[::-1]