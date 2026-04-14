'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        grid = defaultdict(list)

        for i in range(9):
            rows[i] = [0]*10
            for j in range(9):

                if board[i][j] == '.':
                    continue

                num = int(board[i][j])
                if rows[i][num] == 1:
                    return False
                rows[i][num] = 1
        
        for j in range(9):
            cols[j] = [0]*10
            for i in range(9):

                if board[i][j] == '.':
                    continue

                num = int(board[i][j])
                if cols[j][num] == 1:
                    return False
                cols[j][num] = 1

        for r in (0,3,6):
            for c in (0,3,6):
                start = (r,c)
                grid[start] = [0]*10

                for i in range(r,r+3):
                    for j in range(c, c+3):

                        if board[i][j] == '.':
                            continue

                        num = int(board[i][j])
                        if grid[start][num] == 1:
                            return False
                        grid[start][num] = 1
        
        return True


        