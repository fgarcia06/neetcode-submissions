class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute foce solution: go through each row and col till target is found or not

        left = 0
        right = len(matrix) - 1
        mid_row = (left + right) // 2


        while left <= right:
            if target < matrix[mid_row][0]:
                right = mid_row - 1
                mid_row = (left+right) // 2
            elif target > matrix[mid_row][-1]:
                left = mid_row + 1
                mid_row = (left+right) // 2
            # target in mid row
            else:
                start = 0
                end = len(matrix[mid_row]) - 1

                while start <= end:
                    midpoint = (start+end) // 2

                    if target < matrix[mid_row][midpoint]:
                        end = midpoint - 1
                    elif target > matrix[mid_row][midpoint]:
                        start = midpoint + 1
                    else:
                        return True
                    
                    midpoint = (start+end) // 2

                return False
        return False
            

