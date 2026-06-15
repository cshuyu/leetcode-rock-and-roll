# Last updated: 6/15/2026, 9:28:01 PM
1class Solution:
2    def numTrees(self, n: int) -> int:
3        memo = defaultdict(int)
4        def build(total_node):
5            if total_node==0:
6                return 1
7            if total_node in memo:
8                return memo[total_node]
9            total_count = 0
10            for root in range(1, total_node+1):
11                left_count = build(root-1)
12                right_count = build(total_node-root)
13                total_count += left_count*right_count
14                memo[total_node] = total_count
15            return total_count
16        return build(n)
17
18
19        