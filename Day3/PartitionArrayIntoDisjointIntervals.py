'''
Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.

Test cases are generated such that partitioning exists.

'''
from collections import defaultdict
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        curr_max = -1
        n = len(nums)
        in_range_max = defaultdict(int)

        for i in range(n):
            curr_max = max(curr_max, nums[i])
            in_range_max[i] = curr_max

        b = 0
        curr = nums[0]
        for i in range(1,n):
            if curr > nums[i]:
                curr = in_range_max[i]
                b = i
        
        return b+1
        