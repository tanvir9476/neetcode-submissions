class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = i
        for i, num in enumerate(nums):
            if target-num in hashmap:
                j = hashmap[target-num]
                if i != j:
                    return [i, j] if i <= j else [j, i]
        return [i,j] if i <= j else [j, i]
 