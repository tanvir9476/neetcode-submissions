class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for i, op in enumerate(operations):
            if op == "+":
                score1 = stk[-1]
                score2 = stk[-2]
                stk.append(int(score1)+int(score2))
            elif op == "D":
                score1 = stk[-1]
                stk.append(2*int(score1))
            elif op == "C":
                stk.pop()
            else:
                stk.append(int(op))
        print(stk)
        return sum(stk)