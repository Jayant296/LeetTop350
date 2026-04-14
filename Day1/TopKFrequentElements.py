'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


'''
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        count_map = defaultdict(list)

        for num in nums:
            freq[num] += 1
        
        for num, freq in freq.items():
            count_map[freq].append(num)

        result = []
        count = 0
        n = len(nums)

        for freq in range(n, 0, -1):
            for num in count_map[freq]:
                result.append(num)
                count += 1
                if count == k:
                    return result
            


        