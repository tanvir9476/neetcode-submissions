class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        p_map = {"]": '[', "}":"{", ")":"("}
        for p in s:
            if p in "({[":
                stk.append(p)
            else:
                if stk:
                    if stk[-1] == p_map[p]:
                        stk.pop()
                        continue
                stk.append(p)
            # print(stk)
        return True if not stk else False
