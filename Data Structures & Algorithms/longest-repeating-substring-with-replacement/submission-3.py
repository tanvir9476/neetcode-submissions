class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        max_len = 0
        hash_map = collections.defaultdict(int)

        for R in range(len(s)):
            # hash_map = collections.Counter(s[L:R])
            # print(hash_map)
            hash_map[s[R]] += 1




            while (R-L+1-max(hash_map.values(), default=0) > k) :
                hash_map[s[L]]-=1
                L+=1

            max_len = max(max_len, R-L+1)

        
        return max_len