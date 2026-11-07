class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0

        L, maxL, maxR = 0, 0, 0

        for R in range(len(nums)):
            if current_sum < 0:
                current_sum = 0
                L = R

            current_sum += nums[R]

            if current_sum > max_sum:
                max_sum = current_sum
                maxL = L
                maxR = R

        print(nums[L:R+1])

        return max_sum
