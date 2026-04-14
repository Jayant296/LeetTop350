'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using three pointers approach
        start, mid = 0, 0
        end = len(nums)-1

        while mid <= end:
            if nums[mid] == 0:
                nums[start], nums[mid] = nums[mid], nums[start]
                start += 1
                mid += 1

            elif nums[mid] == 2:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1
            
            else:
                mid += 1 # when 1 move mid
            