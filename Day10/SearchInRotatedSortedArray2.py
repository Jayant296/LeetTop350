'''
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        n = len(nums)

        st, end = 0, n-1

        while st <= end:
            mid = (st+end)//2

            if nums[mid] == target:
                return True

            # cant decide which half is sorted, so shrink the search space

            if nums[mid] == nums[st] == nums[end]:
                st += 1
                end -= 1
            
            # choose the sorted half
            
            elif nums[mid] >= nums[st]:
                if nums[st] <= target < nums[mid]:
                    end = mid-1
                else:
                    st = mid + 1
            
            else:
                if nums[mid] < target <= nums[end]:
                    st = mid + 1
                else:
                    end = mid - 1
        
        return False
 
        