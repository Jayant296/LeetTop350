'''
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def peak(st, end):
            if st > end :
                return -1

            mid = (st+end)//2
            
            if mid-1 >= 0 and mid+1 < n:
                if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                    return mid
                elif nums[mid] > nums[mid-1]:
                    return peak(mid+1, end)
                else:
                    return peak(st, mid-1)

            elif mid-1 >= 0:
                if nums[mid] > nums[mid-1]:                  
                    return mid
                else:
                    return peak(st, mid-1)
            else:
                if nums[mid] > nums[mid+1]:
                    return mid
                else:
                    return peak(mid+1, end)

        n = len(nums)

        if n == 1:
            return 0
        
    
        return peak(0, n-1)
