'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, h = -1 , -1
        n = len(nums)

        st, end = 0, n-1
        while st <= end:
            mid = (st+end)//2

            if nums[mid] < target:
                st = mid+1
            else:
                end = mid-1
        
        l = st

        st, end = 0, n-1
        while st <= end:
            mid = (st+end)//2

            if nums[mid] > target:
                end = mid-1
            else:
                st = mid+1
        
        r = end

        return [l,r] if 0 <= l < n and nums[l] == target else [-1,-1]
        