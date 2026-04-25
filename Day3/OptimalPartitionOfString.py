'''Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

'''
from collections import defaultdict
class Solution:
    def partitionString(self, s: str) -> int:
        freq = defaultdict(bool)
        count = 0

        for i in range(len(s)):
            char = s[i]
            if freq[char] :
                count += 1
                freq = defaultdict(bool)
            
            freq[char] = True

        return count+1
