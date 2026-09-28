class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0

        for i in range(n):
            pointA = points[i]

            for j in range(n):
                pointB = points[j]

                if i == j or not (pointA[0] <= pointB[0] and pointA[1] >= pointB[1]):
                    continue

                illegal = False

                for k in range(n):
                    if k == i or k == j:
                        continue

                    pointTmp = points[k]

                    isXContained = pointA[0] <= pointTmp[0] <= pointB[0]
                    isYContained = pointB[1] <= pointTmp[1] <= pointA[1]

                    if isXContained and isYContained:
                        illegal = True
                        break

                if not illegal:
                    ans += 1

        return ans