'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
from collections import defaultdict
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            j, k = i+1, n-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    ans.append((nums[i], nums[j], nums[k]))
                    
                    while j+1 < k and nums[j+1] == nums[j]:
                        j += 1
                    while k-1 > j and nums[k-1] == nums[k]:
                        k -= 1
                    
                    j += 1
                    k -= 1

                elif total > 0:
                    k -= 1
                else:
                    j += 1
        
        return ans


        