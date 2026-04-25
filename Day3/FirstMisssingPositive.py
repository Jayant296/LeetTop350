'''Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 0
        
        for i in range(n):  
            actual_val = nums[i] % (n+1)   

            if actual_val < 0:
                continue
        
            nums[actual_val-1] = (nums[actual_val-1] % (n+1)) + actual_val*(n+1)
        
        for i in range(n):
            if nums[i] // (n+1) != i+1:
                return i+1
        
        return n+1