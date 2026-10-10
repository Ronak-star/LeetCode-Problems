class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        n, m = len(fruits), len(baskets)
        section = int(m**0.5)
        maxV = [0] * (m // section + 1)
        for i, b in enumerate(baskets):
            maxV[i // section] = max(maxV[i // section], b)
            
        used = [False] * m
        unplaced = 0
        for fruit in fruits:
            choose = -1
            pos = 0
            while pos < m:
                idx = pos // section
                if maxV[idx] < fruit:
                    pos = (idx + 1) * section
                    continue
                    
                for k in range(pos, min((idx + 1) * section, m)):
                    if not used[k] and baskets[k] >= fruit:
                        choose = k
                        break
                        
                if choose != -1:
                    break
                pos = (idx + 1) * section
                
            if choose == -1:
                unplaced += 1
            else:
                used[choose] = True
                
                # We need to update the max value of the block
                block_start = (choose // section) * section
                block_end = min(block_start + section, m)
                current_max = 0
                for i in range(block_start, block_end):
                    if not used[i]:
                        current_max = max(current_max, baskets[i])
                maxV[choose // section] = current_max
                
        return unplaced