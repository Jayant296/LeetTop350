'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = defaultdict(int)
        freq_s2 = defaultdict(int)
        n = len(s1)
        st = 0

        for i in s1:
            freq_s1[i] += 1

        for i, ch in enumerate(s2):
            if ch in Freq_:


        for i, val in freq_s1.items():
            if freq_s2[i] < freq_s1[i]:
                return False

        return True


        