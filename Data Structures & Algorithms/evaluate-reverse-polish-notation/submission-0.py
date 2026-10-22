class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stk.append(int(token))
            else:
                b = int(stk.pop())
                a = int(stk.pop())
                if token == "+":
                    stk.append(int(a+b))
                elif token == "-":
                    stk.append(int(a-b))
                elif token == "*":
                    stk.append(int(a*b))
                elif token == "/":
                    stk.append(int(a/b))

        return stk[-1]