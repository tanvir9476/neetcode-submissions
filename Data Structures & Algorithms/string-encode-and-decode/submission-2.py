# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         return "".join(f"{len(s)}#{s}" for s in strs) # "4#xxxx2#xx"

#     def decode(self, s: str) -> List[str]:
#         ans = []
#         i = 0

#         while i < len(s):
#             j = i
#             while s[j] != "#":
#                 j+=1
#             length = int(s[i:j])
#             ans.append(s[j+1:j+1+length])
#             i += j + length + 1
#         return ans
class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":        # find end of the length number
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length        # jump past this string entirely
        return res