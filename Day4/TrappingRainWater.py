'''

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

'''
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        trapped = 0
        stack = []

        for i in range(n):

            while stack and height[stack[-1]] < height[i]:
                bottom = stack.pop()

                if not stack:
                    break

                left = stack[-1]
                width = i - left - 1
                bounded_height = min(height[left], height[i]) - height[bottom]

                water = bounded_height*width

                trapped += water
            
            stack.append(i)
        
        return trapped
        