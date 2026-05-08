'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            if nums[l] < nums[r]:
                break

            mid = (l + r)//2

            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid

        if target <= nums[n-1]:
            st = l
            end = n-1
        else:
            st = 0
            end = l-1 

        while st <= end:
            if st == end:
                return st if nums[st] == target else -1 

            mid = (st+end)//2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                end = mid - 1
            else:
                st = mid+1

        return -1
        
         

        


            

