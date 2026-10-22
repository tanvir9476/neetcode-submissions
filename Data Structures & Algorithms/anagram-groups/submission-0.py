class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} # {char : occ} : index

        for i, s in enumerate(strs):
            s_map = tuple(sorted(Counter(s).items()))
            if s_map in hashmap:
                hashmap[s_map].append(i)
            else:
                hashmap[s_map] = [i]

        ans = []
        for anagram in hashmap:
            sub_ans = [strs[i] for i in hashmap[anagram]]
            ans.append(sub_ans)

        return ans