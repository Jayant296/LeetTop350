'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        slopes = defaultdict(None)
        n = len(points)
        max_points = float('-inf')

        for i in range(n):
            origin = tuple(points[i])
            slopes[origin] = defaultdict(int)
            for j in range(n):
                if i == j :
                    continue

                point = points[j]
                slope = (point[1]-origin[1])/(point[0]-origin[0]) if (point[0]-origin[0]) != 0 else 'v'

                slopes[origin][slope] += 1
            
            max_points = max(max_points, max(slopes[origin].values()) if slopes[origin] else float('-inf'))

        return max_points+1 if max_points != float('-inf') else len(points)
