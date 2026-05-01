'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
'''
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        st = 0
        count0 = 0
        max_len = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1

                if count0 == 2:
                    max_len = max(max_len, i-st-1)

                    while count0 == 2:
                        if nums[st] == 0:
                            count0 -= 1
                            st += 1
                            break
                        st += 1
        
        max_len = max(max_len, len(nums)-st-1)
        return max_len


        