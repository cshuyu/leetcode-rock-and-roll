# Last updated: 3/30/2026, 11:54:59 PM
# Monotonical stack
1'''
2Time Complexity: sort time is O(nlogn), going through stack is O(n)
3Total time is O(nlogn)
4Space Complexity: sort is O(n), going through stack is also O(n)
5'''
6class Solution:
7    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
8        cars = sorted(zip(position, speed), reverse=True)
9        stack = []
10        for p, s in cars:
11            curr_time = (target-p)/s
12            if not stack or (stack and stack[-1]<curr_time):
13                stack.append(curr_time)
14        return len(stack)
15            
16