class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num != '.':
                    b = (r // 3) * 3 + (c // 3)

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

        def solve():

            for r in range(9):
                for c in range(9):

                    if board[r][c] == '.':

                        b = (r // 3) * 3 + (c // 3)

                        for num in "123456789":

                            if (num not in rows[r] and
                                num not in cols[c] and
                                num not in boxes[b]):

                                board[r][c] = num
                                rows[r].add(num)
                                cols[c].add(num)
                                boxes[b].add(num)

                                if solve():
                                    return True

                                # Backtrack
                                board[r][c] = '.'
                                rows[r].remove(num)
                                cols[c].remove(num)
                                boxes[b].remove(num)

                        return False

            return True

        solve()