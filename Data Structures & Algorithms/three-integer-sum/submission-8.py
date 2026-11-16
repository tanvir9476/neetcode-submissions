class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nov 16 hashmap
        res = set()
        nums.sort()
        count = collections.Counter(nums)

        for i in range(len(nums)):
            count[nums[i]] -= 1
            
            for j in range(i+1, len(nums)):
                count[nums[j]] -= 1
                target = -(nums[i]+nums[j])
                if count[target]> 0:
                    res.add(tuple(sorted([nums[i], nums[j], target])))
                count[nums[j]] += 1
            count[nums[i]] += 1

        return [list(tup) for tup in res]