'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = Counter(t)
        freq_s = defaultdict(int)
        n = len(t)
        st = 0
        best = [-1, -1]
        min_len = float('inf')

        if min_len < n:
            return ''
        
        for i, ch in enumerate(s):
            freq_s[ch] += 1
            window = i-st+1
            
            if window >= n:
                isContain = True

                for key, val in freq_t.items():
                    if freq_s[key] < val:
                        isContain = False
                        break

                if isContain:
                    while isContain:
                        if min_len > window:
                            min_len = window
                            best =  [st,i]

                        if freq_s[s[st]] > freq_t[s[st]]:
                            freq_s[s[st]] -= 1
                            st += 1
                            window = i-st+1
                        else:
                            break
        

        return s[best[0]:best[-1]+1] if min_len != float('inf') else ''
        

        
                
        