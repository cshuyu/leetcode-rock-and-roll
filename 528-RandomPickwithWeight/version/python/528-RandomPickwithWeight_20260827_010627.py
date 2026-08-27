# Last updated: 8/27/2026, 1:06:27 AM
# Random pick with weight
1"""
2O(Time): O(logn)
3O(Space): O(n)
4"""
5class Solution:
6
7    def __init__(self, w: List[int]):
8        n = len(w)
9        self.prefix_sum = [0]*(n+1)
10        for i in range(1, n+1):
11            self.prefix_sum[i] = self.prefix_sum[i-1] + w[i-1]
12
13    def pickIndex(self) -> int:
14        target = random.randint(1, self.prefix_sum[-1])
15        def binarySearch(lst, target):
16            left = 0
17            right = len(lst)-1
18            while left<right:
19                mid = left + (right-left)//2
20                if lst[mid]==target:
21                    return mid
22                elif lst[mid]<target:
23                    left = mid+1
24                else:
25                    right = mid
26            return right
27        idx = binarySearch(self.prefix_sum, target)
28        return idx-1
29        
30
31
32# Your Solution object will be instantiated and called as such:
33# obj = Solution(w)
34# param_1 = obj.pickIndex()