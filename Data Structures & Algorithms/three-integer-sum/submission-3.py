class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans_set = set()
        nums_set = {val:idx for idx, val in enumerate(nums)}

        for i in range(len(nums)):
            for j in range(len(nums)):
                # k = 0
                # while i != j and k < len(nums) :
                nums_k = - (nums[i] + nums[j])
                if nums_k in nums_set and nums_set[nums_k] != i and nums_set[nums_k] != j and i != j:
                    ans_set.add(tuple(sorted([nums[i], nums[j], nums_k])))
                    # k+=1
        
        return [list(triplets) for triplets in ans_set]