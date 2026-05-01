'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        st = 0
        min_len = float('inf')
        pref = 0

        for i, val in enumerate(nums):
            pref += val

            if pref >= target:

                while pref >= target:
                    min_len = min(min_len, i-st+1)

                    pref -= nums[st]
                    st += 1

        return min_len if min_len != float('inf') else 0 
        