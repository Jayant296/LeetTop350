'''
There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

'''
from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cuts = defaultdict(int)

        for row in wall:
            curr = 0
            for brick in range(len(row)-1):
                curr += row[brick]
                cuts[curr] += 1
        
        if not cuts.values():
            return len(wall)

        return len(wall) - max(cuts.values())


        