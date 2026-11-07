class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS, COLS = len(matrix), len(matrix[0])
        row_flag = [False] * ROWS
        col_flag = [False] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    row_flag[r] = True
                    col_flag[c] = True
        
        for r, flag in enumerate(row_flag):
            if flag:
                for c in range(COLS):
                    matrix[r][c] = 0
        
        for c, flag in enumerate(col_flag):
            if flag:
                for r in range(ROWS):
                    matrix[r][c] = 0