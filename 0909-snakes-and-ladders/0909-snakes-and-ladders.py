import collections

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)

        def get_coordinates(square_num, size_n):
            num_zero_indexed = square_num - 1
            row_from_bottom = num_zero_indexed // size_n

            r = (size_n - 1) - row_from_bottom

            if row_from_bottom % 2 == 0:
                c = num_zero_indexed % size_n
            else:
                c = (size_n - 1) - (num_zero_indexed % size_n)

            return r, c

        queue = collections.deque()
        queue.append((1, 0))
        visited = {1}

        while queue:
            current_square, moves = queue.popleft()

            if current_square == n * n:
                return moves

            for i in range(1, 7):
                next_square_candidate = current_square + i

                if next_square_candidate > n * n:
                    break

                r, c = get_coordinates(next_square_candidate, n)

                final_destination = next_square_candidate

                if board[r][c] != -1:
                    final_destination = board[r][c]

                if final_destination not in visited:
                    visited.add(final_destination)
                    queue.append((final_destination, moves + 1))

        return -1