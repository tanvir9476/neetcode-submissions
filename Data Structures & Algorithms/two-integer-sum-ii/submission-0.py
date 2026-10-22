class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index0 = 0
        index1 = len(numbers) - 1
        while numbers[index0] + numbers[index1] != target:
            if numbers[index0] + numbers[index1] > target:
                index1 -= 1
            elif numbers[index0] + numbers[index1] < target:
                index0 += 1
            else:
                break
        return [index0+1, index1+1]
