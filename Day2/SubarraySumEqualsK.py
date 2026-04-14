'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

'''
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)

        count = 0
        curr = 0
        freq[0] = 1

        for num in nums:
            curr += num

            count += freq[curr-k]

            freq[curr] += 1

        return count
            

        