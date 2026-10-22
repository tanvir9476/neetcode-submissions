class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = ""
        for c in s:
            if ("A" <= c <= "Z") or ("a" <= c <= "z") or ("0" <= c <= "9"):
                new_s += c.lower()

        s_rev = new_s[::-1]
        # print(s_rev)
        for i in range(len(new_s)):
            if new_s[i] != s_rev[i]:
                return False
        return True