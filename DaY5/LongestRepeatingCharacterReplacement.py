'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        st = 0
        longest = 0

        for i,ch in enumerate(s):
            freq[ch] += 1
            window = i-st+1

            if window - max(freq.values()) > k:
                longest = max(longest, window-1)

                while window - max(freq.values()) > k:
                    freq[s[st]] -= 1
                    st += 1
                    window = i-st+1
        
        longest = max(longest, len(s)-st)

        return longest
                
                

                    

                
        