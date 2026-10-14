class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()

        m, n = len(players), len(trainers)
        i, j = 0, 0
        count = 0

        while i < m and j < n:
            if players[i] <= trainers[j]:
                count += 1
                i += 1

            j += 1

        return count