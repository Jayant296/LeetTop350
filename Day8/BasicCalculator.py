'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
'''
class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        num = 0
        sign = 1
        result = 0

        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch)
            
            elif ch == '+':
                result += num*sign
                num = 0
                sign = 1
            
            elif ch == '-':
                result += num*sign
                num = 0
                sign = -1
            
            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                num, result = 0, 0
                sign = 1
            
            elif ch == ')':
                result += num*sign
                num = 0
                result *= stack.pop()
                result += stack.pop()
        
        return result + num*sign
