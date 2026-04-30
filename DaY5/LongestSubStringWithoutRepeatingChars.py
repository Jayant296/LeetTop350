'''
Given a string s, find the length of the longest substring without duplicate characters'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        longest = float('-inf')
        curr = 0

        for i, val in enumerate(s):
            if val in freq and freq[val] >= curr:
                longest = max(longest, i - curr)
                curr = freq[val] + 1

            freq[val] = i

        longest = max(longest, len(s) - curr)
        
        return longest

