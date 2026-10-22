class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        running_max = -1
        for i in range(len(arr)-1,-1,-1):
            arr_i = arr[i]
            arr[i] = running_max
            running_max = max(running_max, arr_i)
        return arr