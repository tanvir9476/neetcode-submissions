class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} # {char : occ} : index

        for i, s in enumerate(strs):
            s_map = tuple(sorted(Counter(s).items()))
            if s_map in hashmap:
                hashmap[s_map].append(s)
            else:
                hashmap[s_map] = [s]
        # print(hashmap.values())
        return list(hashmap.values())