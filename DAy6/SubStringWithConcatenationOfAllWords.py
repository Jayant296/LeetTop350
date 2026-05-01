'''
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        freq_w = Counter(words)
        w = len(words[0])
        n = w*(len(words))
        ans = []

        start_chars = defaultdict(bool)

        for word in words:
            start_chars[word[0]] = True

        for i in range(0,len(s)-n+1):

            if not start_chars[s[i]]:
                continue

            freq_s = defaultdict(int)

            for j in range(i, i+n, w):
                freq_s[s[j:j+w]] += 1

            isConcat = True

            for key, val in freq_w.items():
                if freq_s[key] != val:
                    isConcat = False
                    break
            
            if isConcat:
                ans.append(i)
        
        return ans
            


            
            


        