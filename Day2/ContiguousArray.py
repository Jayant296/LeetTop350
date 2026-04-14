'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        curr = 0
        sum_index = {0:-1}
        max_len = 0

        for i, num in enumerate(nums):
            curr += 1 if num == 1 else -1
            
            if curr in sum_index:
                max_len = max(max_len, i-sum_index[curr])
            else:
                sum_index[curr] = i
        
        return max_len


         
        