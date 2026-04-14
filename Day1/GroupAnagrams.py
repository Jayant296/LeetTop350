'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
'''

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            key = [0]*26
            for c in word:
                key[ord(c)-ord('a')] += 1
            
            d[tuple(key)].append(word)
        return list(d.values())
        


