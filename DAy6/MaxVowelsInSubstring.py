'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        st = 0
        freq = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        max_vowel = 0

        for i, val in enumerate(s):
            if val in freq:
                freq[val] += 1
            
            if i-st + 1 == k:
                max_vowel = max(max_vowel, sum(freq.values()))

                if s[st] in freq:
                    freq[s[st]] -= 1
                
                st += 1
        
        max_vowel = max(max_vowel, sum(freq.values()))
        return max_vowel
        