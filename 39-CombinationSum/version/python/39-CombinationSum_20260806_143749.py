# Last updated: 8/6/2026, 2:37:49 PM
# Backtracking: combination_sum
1"""
2Time: O(n^(target/min(n)))
3Space: O(n), sort's space complexity is O(n), the backtracking stack complexity is O(target/min(n))
4"""
5class Solution:
6    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
7        res = []
8        candidates.sort()
9
10        def helper(start, remaining, path):
11            if remaining == 0:
12                res.append(path[:])
13                return
14            for i in range(start, len(candidates)):
15                if candidates[i] > remaining:
16                    break
17                path.append(candidates[i])
18                helper(i, remaining-candidates[i], path)
19                path.pop()
20            
21        helper(0, target, [])
22        return res