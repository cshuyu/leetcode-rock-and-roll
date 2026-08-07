# Last updated: 8/6/2026, 10:51:23 PM
1"""
2Time: O(n*2^n)
3Space: O(n)
4"""
5class Solution:
6    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
7        res = []
8        candidates.sort()
9
10        def helper(start, remaining, path):
11            if remaining==0:
12                res.append(path[:])
13            for i in range(start, len(candidates)):
14                if candidates[i] > remaining:
15                    break
16                if i>start and candidates[i]==candidates[i-1]:
17                    continue
18                path.append(candidates[i])
19                helper(i+1, remaining-candidates[i], path)
20                path.pop()
21        
22        helper(0, target, [])
23        return res