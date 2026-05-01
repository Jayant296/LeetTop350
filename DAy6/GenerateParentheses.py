'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backTrack(curr, open_used, close_used):
            if len(curr) == 2*n:
                res.append(curr)
                return 
            
            # choise 1 '('
            if open_used < n:
                backTrack(curr + '(', open_used+1, close_used)
            
            # choise 2 ')'
            if close_used < open_used:
                backTrack(curr + ')', open_used, close_used+1)

            return 
        
        res = []
        backTrack('',0,0)

        return res
        