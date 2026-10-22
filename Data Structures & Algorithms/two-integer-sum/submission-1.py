class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # num : index
        for i, num in enumerate(nums):
            d = target - num
            if d in hashmap:
                return [hashmap[d], i]
            else:
                hashmap[num] = i
 