'''
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('-inf')

        for i in range(n):
            j, k = i+1, n-1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total > target:
                    k -= 1
                else:
                    j += 1
                
                closest = total if abs(target - total) < abs(target - closest) else closest
                
                if closest == target:
                    return target
        
        return closest
        