class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        n = len(tops)

        def check(target):
            rotations_top = 0
            rotations_bottom = 0
            for i in range(n):
                if tops[i] != target and bottoms[i] != target:
                    return math.inf
                elif tops[i] != target:
                    rotations_top += 1
                elif bottoms[i] != target:
                    rotations_bottom += 1
                
            return min(rotations_top, rotations_bottom)
        rotations = check(tops[0])

        if tops[0] != bottoms[0]:
            rotations = min(rotations, check(bottoms[0]))
        
        return rotations if rotations != math.inf else -1