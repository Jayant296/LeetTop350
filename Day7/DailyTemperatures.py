'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0]*n

        for i,t in enumerate(temperatures):
            
            while stack and stack[-1][0] < t:
                temp, indx = stack.pop()

                ans[indx] = i-indx
            
            stack.append([t,i])
        
        return ans

        