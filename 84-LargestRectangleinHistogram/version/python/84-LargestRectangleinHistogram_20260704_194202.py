# Last updated: 7/4/2026, 7:42:02 PM
# Monotonic Stack
1"""
2O(Time): O(n)
3O(Space): O(n)
4We use a monotonic stack because it perfectly pairs an element with its immediate smaller neighbors without needing to search for them. It converts a problem that natively requires looking backward and forward into a single, continuous forward-marching timeline, compressing an $O(n^2)$ search into a highly efficient $O(n)$ stream.
5Left boundary is stack[-1] and right boundy is the one less than it
6"""
7class Solution:
8    def largestRectangleArea(self, heights: List[int]) -> int:
9        stack = [0]
10        # add a dummy nodes with the top height 0 at the end
11        heights.append(0)
12        max_area = 0
13
14        for i in range(1, len(heights)):
15            while stack and heights[stack[-1]]>heights[i]:
16                pop_idx = stack.pop()
17                height = heights[pop_idx]
18                if stack:
19                    width = i-stack[-1]-1
20                else:
21                    width = i
22                curr_area = height*width
23                max_area = max(max_area, curr_area)
24            stack.append(i)
25        
26        return max_area
27