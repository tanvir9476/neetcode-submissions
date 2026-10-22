class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if self.validSet(row) == False:
                return False
        for i in range(9):
            col = [board[j][i] for j in range(9)]
            if self.validSet(col) == False:
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = board[i+0][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                if self.validSet(box) == False:
                    return False
        return True



    def validSet(self, S, delim=".") -> bool:
        S_Counter = Counter(S)
        del S_Counter[delim]
        return S_Counter == Counter() or (len(set(S_Counter.values())) == 1 and sum(set(S_Counter.values())) == 1)

    
        