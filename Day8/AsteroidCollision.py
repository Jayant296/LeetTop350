'''
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a < 0:
                if stack and stack[-1] > 0:
                    destroyed = False
                    while stack and stack[-1] > 0:
                        if abs(stack[-1]) == abs(a):
                            stack.pop()
                            destroyed = True
                            break
                        elif abs(stack[-1]) > abs(a):
                            destroyed = True
                            break
                        else:
                            stack.pop()
                    if not destroyed:
                        stack.append(a)
                else:
                    stack.append(a)
            else:
                stack.append(a)
        
        return stack

                

        return stack

        