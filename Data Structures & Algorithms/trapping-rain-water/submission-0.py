class Solution:
    def trap(self, height: List[int]) -> int:
        height = [0] + height + [0]
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        minLR = [0] * len(height)
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
        # print(maxLeft)
        for i in range(len(height)-2, -1, -1):
            # print(i)
            maxRight[i] = max(maxRight[i+1], height[i+1])
        # print(maxRight)
        for i in range(len(height)):
            minLR[i] = max(min(maxLeft[i], maxRight[i])-height[i], 0)
        # print(range(0, len(height)-1, -1))
        return sum(minLR)