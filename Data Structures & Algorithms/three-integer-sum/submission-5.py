class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = set()
        for i, num in enumerate(nums):
            target = -num
            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[l]+nums[r]<target:
                    l+=1
                elif nums[l]+nums[r]>target:
                    r-=1
                else:
                    ans.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                    l+=1
                    r-=1

        return [list(triplet) for triplet in ans]