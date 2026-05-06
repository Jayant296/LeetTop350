'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        max_area = 0

        for i in range(n+1):
            h = heights[i] if i < n else 0
            
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                
                max_area = max(max_area, height*width)
            
            stack.append(i)
        
        return max_area

        