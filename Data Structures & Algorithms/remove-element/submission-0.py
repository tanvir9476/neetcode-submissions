class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        cng_idx = []
        for i in range(len(nums)):
            if nums[i] == val:
                pass
            else:
                nums[k] = nums[i]
                k+=1
        # print(cng_idx)
        return k