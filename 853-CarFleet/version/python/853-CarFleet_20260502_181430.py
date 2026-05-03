# Last updated: 5/2/2026, 6:14:30 PM
# Monotonic Stack: 2nd Practice
1'''
2Clarify 
31) Input integrity: will the value of position be unique; will speed be zero? 
42) Data precision: should I concern about the slight difference of time, or keeping everythingas integers is fine?
53) Data range: will the position be over the target?
6'''
7class Solution:
8    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
9        cars = sorted(zip(position, speed), reverse=True)
10        stack = []
11
12        for p, s in cars:
13            time = (target-p)/s
14            if not stack or time>stack[-1]:
15                stack.append(time)
16        
17        return len(stack)
18
19        