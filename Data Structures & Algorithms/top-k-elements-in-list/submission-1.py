class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        # sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

        return [num for num, _ in count.most_common(k)]