class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_streak = 0
        streak = 0
        for num in nums:
            if num == 1:
                streak += 1
            else:
                # max_streak = max(max_streak, streak)
                streak = 0
            # print(f"streak: {streak}")
            # print(f"max_streak: {max_streak}")
            max_streak = max(max_streak, streak)
        return max_streak