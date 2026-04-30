'''
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.
'''
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        st = 0
        pref = nums[0]
        max_len = 1
        curr = k

        for i in range(1, len(nums)):
            pref += nums[i]
            cost = nums[i] * (i-st+1) - pref

            if cost > k:
                max_len = max(max_len, i-st)

                while cost > k:
                    pref -= nums[st] 
                    st += 1
                    cost = nums[i]*(i-st+1) - pref
        
        max_len = max(max_len, len(nums)-st)
        return max_len



        
        max_len = max(max_len, len(nums)-st)

        return max_len



        