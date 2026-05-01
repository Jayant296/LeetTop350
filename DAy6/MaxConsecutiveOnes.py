'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        st = 0
        count0 = 0
        max_len = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1

                if count0 > k:
                    max_len = max(max_len, i-st)

                    while count0 > k:
                        if nums[st] == 0:
                            count0 -= 1
                        
                        st += 1
        
        max_len = max(max_len, len(nums)-st)
        return max_len
        