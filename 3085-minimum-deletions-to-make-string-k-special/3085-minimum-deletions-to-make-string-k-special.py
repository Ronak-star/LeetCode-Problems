class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = defaultdict(int)
        for c in word:
            cnt[c] += 1

        counts = list(cnt.values())
        res = len(word)

        for base_freq in counts:
            deleted = 0
            for freq in counts:
                if freq < base_freq:
                    deleted += freq
                elif freq > base_freq + k:
                    deleted += freq - (base_freq + k)
            res = min(res, deleted)
        return res