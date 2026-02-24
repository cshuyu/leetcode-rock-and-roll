# Last updated: 2/23/2026, 6:45:51 PM
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroidStack = []
        for star in asteroids:
            while asteroidStack and star<0<asteroidStack[-1]:
                if asteroidStack[-1] == -1 * star:
                    asteroidStack.pop()
                elif asteroidStack[-1]< -1 * star:
                    asteroidStack.pop()
                    continue
                break
            else:
                asteroidStack.append(star)
        
        return asteroidStack


        