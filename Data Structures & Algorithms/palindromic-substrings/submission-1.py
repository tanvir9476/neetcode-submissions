class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        hash_set = set()

        for i in range(len(s)):
            # odd
            l, r = i, i

            while l>=0 and r<len(s) and s[l] == s[r]:
                # if (l, r) not in hash_set:
                #     hash_set.add((l, r))
                res +=1
                r+=1
                l-=1

            # even
            l, r = i, i+1

            while l>=0 and r<len(s) and s[l] == s[r]:
                # if (l, r) not in hash_set:
                #     hash_set.add((l, r))
                res +=1
                r+=1
                l-=1

        return res