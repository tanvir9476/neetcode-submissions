class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_left, row_right = 0, len(matrix[0])-1
        left, right = 0, len(matrix)-1

        while left <= right:
            mid = (left + right) // 2
            if target < matrix[mid][row_left]:
                right = mid - 1
            elif target > matrix[mid][row_right]:
                left = mid + 1
            else:
                while row_left <= row_right:
                    row_mid = ( row_left + row_right) //2
                    if target < matrix[mid][row_mid]:
                        row_right = row_mid - 1
                    elif target > matrix[mid][row_mid]:
                        row_left = row_mid + 1 
                    elif target == matrix[mid][row_mid]:
                        return True
            #         print(f"row_left: {row_left}")
            #         print(f"row_right: {row_right}")
            # print(f"left: {left}")
            # print(f"right: {right}")
        return False

        
