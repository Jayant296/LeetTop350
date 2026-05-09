'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        st, end = 0, n-1

        while st < end:
            mid = (st+end)//2

            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] == nums[mid+1]:
                st = mid+2
            else:
                end = mid

        return nums[st]
        
        