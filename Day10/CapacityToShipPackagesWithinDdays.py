'''
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
'''
import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        total = sum(weights)
        l, r = max(weights), total

        while l <= r:
            mid = (l+r)//2
            time = 0
            curr = 0

            for i in range(n):
                curr += weights[i]

                if curr > mid:
                    time += 1
                    curr = weights[i]
            
            time += 1

            if time > days:
                l = mid+1
            else:
                r = mid-1
        
        return l
            
        