'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = 0
        prod = 1

        for i in nums:
            if i == 0:
                zeros += 1
            else:
                prod *= i
        
        if zeros > 1:
            return [0]*n

        ans = [0]*n
        if zeros == 1:
            for i in range(n):
                if nums[i] == 0:
                    ans[i] = prod
                    return ans
        
        for i in range(n):
            ans[i] = int(prod/nums[i])
        
        return ans
             

        