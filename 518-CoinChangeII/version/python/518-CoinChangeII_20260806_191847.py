# Last updated: 8/6/2026, 7:18:47 PM
# TopDown DFS + memo
1"""
2Time: O(n*amount)
3Space: O(n*amount)
4"""
5class Solution:
6    def change(self, amount: int, coins: List[int]) -> int:
7        memo = {}
8
9        def helper(start, remaining):
10            if (start, remaining) in memo:
11                return memo[(start, remaining)]
12            if remaining == 0:
13                return 1
14            if remaining<0 or start == len(coins):
15                return 0
16            res = helper(start, remaining-coins[start]) + helper(start+1, remaining)
17            memo[(start, remaining)] = res
18            return res
19
20        return helper(0, amount)
21                
22