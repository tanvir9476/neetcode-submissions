class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if len(s1) == len(s2):
            hashmap_s1 = Counter(s1)
            hashmap_s2 = Counter(s2)
            return hashmap_s1 == hashmap_s2
        elif len(s1) < len(s2):
            hashmap_s1 = Counter(s1)
            for i in range(0, len(s2)-len(s1)+1):
                l, r = i, i+len(s1)
                hashmap_s2 = Counter(s2[l:r])
                # print("s1", hashmap_s1)
                # print("s2", l, r, hashmap_s2)
                if hashmap_s1 == hashmap_s2:
                    return True

        return False
