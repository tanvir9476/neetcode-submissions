class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1 
        curr_min = nums[left]
        while left <= right:
            # mid = (left + right) //2
            if nums[left] < nums[right]:
                curr_min = min(curr_min, nums[left])
                break
            else:
                mid = (left + right) //2
                curr_min = min(curr_min, nums[mid])
                if nums[left] <= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return curr_min