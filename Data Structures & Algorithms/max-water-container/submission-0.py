class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_amount = 0
        while l <= r:
            curr_amount = (r - l) * min (heights[l], heights[r])
            max_amount = max(curr_amount, max_amount)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] >= heights[r]:
                r -= 1

        return max_amount