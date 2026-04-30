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
            if ch in freq_s1:
                freq_s2[ch] += 1
                window = i-st+1
                if window == n:
                    isContain = True
                    for i,val in freq_s1.items():
                        if freq_s2[i] < freq_s1[i]:
                            isContain = False
                            break

                    if isContain:
                        return True

                    freq_s2[s2[st]] -= 1
                    st += 1
            else:
                st = i+1
                freq_s2 = defaultdict(int)
        
        return False
        
        

        