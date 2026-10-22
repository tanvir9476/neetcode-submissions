class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        import itertools

        nums = list(itertools.chain.from_iterable(matrix))

        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1 # 3
            elif nums[mid] < target:
                left = mid + 1 # 3
            else:
                return True
        return False