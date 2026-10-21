
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)

        if numFriends == 1:
            return word

        max_len = n - numFriends + 1
        res = ""

        for i in range(n):
            current = word[i:i + max_len]

            if current > res:
                res = current

        return res

