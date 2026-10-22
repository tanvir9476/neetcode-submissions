class MinStack:

    def __init__(self):
        self.stk = []
        self.minstk = [2**31 -1]

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.minstk.append(min(val, self.minstk[-1]))

    def pop(self) -> None:
        self.stk.pop()
        self.minstk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]
