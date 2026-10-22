class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None] * n
        pre = 1
        post = 1

        ans[0] = pre

        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            post *= nums[i+1]
            ans[i] = ans[i] * post

        print(ans)
        return ans