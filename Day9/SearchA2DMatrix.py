'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        def search(l, r):
            if l > r :
                return False

            mid = (l+r)//2

            row, col = mid // n, mid % n
            val = matrix[row][col]

            if val == target:
                return True

            elif val > target:
                return search(l, mid-1)

            else:
                return search(mid+1, r)
            
        return search(0, m*n - 1)
        
        