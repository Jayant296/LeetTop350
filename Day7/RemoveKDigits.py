'''
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
'''


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i in num:
            while stack and stack[-1] >  i and k > 0:
                stack.pop()
                k -= 1
            stack.append(i)
        
        ans = ''.join(stack[:len(stack)-k])
        ans = ans.lstrip('0')

        return ans if ans else '0'  
        