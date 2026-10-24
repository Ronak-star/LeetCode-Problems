class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        counts = collections.Counter(words)
        length = 0
        center_found = False

        for word, count_w in counts.items():
            if word[0] == word[1]:
                length += (count_w // 2) * 4
                
                if count_w % 2 == 1:
                    center_found = True
                
            else:
                rev_word = word[1] + word[0]
                if word < rev_word:
                    if rev_word in counts:
                        num_outer_pairs = min(counts[word], counts[rev_word])
                        length += num_outer_pairs * 4
        
        if center_found:
            length += 2
        
        return length