class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        max_dist = 0
        countN, countS, countE, countW = 0, 0, 0, 0

        for i, move in enumerate(s):
            if move == 'N':
                countN += 1
            elif move == 'S':
                countS += 1
            elif move == 'E':
                countE += 1
            else : # move == 'W'
                 countW += 1
            
            L = i + 1
            
            min_pairs = min(countN, countS) + min(countE, countW)

            current_dist = 0
            if k >= min_pairs:
                current_dist = L
            else:
                base_dist_from_non_conflicting = L - 2 * min_pairs
                current_dist = base_dist_from_non_conflicting + 2 * k
            
            max_dist = max(max_dist, current_dist)

        return max_dist