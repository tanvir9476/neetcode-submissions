class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        l, r = 0, 0
        substring_length = 0
        for i, c in enumerate(s):
            if c not in hashSet:
                hashSet.add(c)
                r=i
                substring_length = max(substring_length, r-l+1)
            else:
                while c in hashSet:
                    hashSet.remove(s[l])
                    l+=1
                hashSet.add(c)
                # substring_length = max(substring_length, r-l+1)
            # s[l:r]
        # print(substring_length, s[l:r])
        return substring_length