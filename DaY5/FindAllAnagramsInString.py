'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq_p = Counter(p)
        freq_s = defaultdict(int)
        st = 0
        n = len(p)
        ans = []

        for i, ch in enumerate(s):
            if ch in freq_p:
                freq_s[ch] += 1
                window = i - st + 1

                if window == n:
                    isContain = True
                    for key, val in freq_p.items():
                        if freq_p[key] > freq_s[key]:
                            isContain = False
                            break

                    if isContain:
                        ans.append(st)

                    freq_s[s[st]] -= 1
                    st += 1
            else:
                st = i+1
                freq_s = defaultdict(int)

        return ans
        
        