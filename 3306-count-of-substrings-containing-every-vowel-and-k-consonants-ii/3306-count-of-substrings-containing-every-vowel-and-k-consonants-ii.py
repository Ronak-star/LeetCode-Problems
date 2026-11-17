class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        def count_at_most(k):
            if k < 0:
                return 0

            vowels = "aeiou"
            last_seen = {v: -1 for v in vowels}

            left = 0
            consonants = 0
            total = 0

            for right, char in enumerate(word):

                if char in vowels:
                    last_seen[char] = right
                else:
                    consonants += 1

                while consonants > k:
                    if word[left] not in vowels:
                        consonants -= 1
                    left += 1

                min_vowel = min(last_seen.values())

                if min_vowel >= left:
                    total += min_vowel - left + 1

            return total

        return count_at_most(k) - count_at_most(k - 1)