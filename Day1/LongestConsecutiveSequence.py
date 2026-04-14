'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

'''
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        isPresent = defaultdict(bool)

        for i in nums:
            isPresent[i] = True
        
        max_seq = 0

        for i in nums:
            if not isPresent[i]:
                continue

            count = 1
            j = i-1
            while isPresent[j]:
                count += 1
                isPresent[j] = False
                j -= 1

            j = i+1
            while isPresent[j]:
                count += 1
                isPresent[j] = False
                j += 1
            
            max_seq = max(max_seq, count)
            isPresent[i] = False

        return max_seq