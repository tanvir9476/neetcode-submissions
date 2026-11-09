class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        from bisect import bisect_left, bisect_right
        start = sorted([flower[0] for flower in flowers])
        end = sorted([flower[1] for flower in flowers])

        ans = []

        for person in people:
            ans.append(bisect_right(start, person) - bisect_left(end, person))
        # print(ans)
        return ans
