'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                k, l = j+1, n-1

                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]

                    if total == target:
                        ans.append((nums[i], nums[j], nums[k], nums[l]))

                        while k+1 < l and nums[k+1] == nums[k]:
                            k += 1
                        while l-1 > k and nums[l-1] == nums[l]:
                            l -= 1
                        
                        k += 1
                        l -= 1
                    
                    elif total > target:
                        l -= 1
                    else :
                        k += 1
        
        return ans
        