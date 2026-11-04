class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrk(i, cur, total):
            if total == target:
                result.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            backtrk(i, cur, total + nums[i])

            cur.pop()
            backtrk(i+1, cur, total)

        backtrk(0, [], 0)

        return result