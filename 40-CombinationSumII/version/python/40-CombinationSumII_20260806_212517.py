# Last updated: 8/6/2026, 9:25:17 PM
1class Solution:
2    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
3        res = []
4        candidates.sort()
5
6        def helper(start, remaining, path):
7            if remaining==0:
8                res.append(path[:])
9            for i in range(start, len(candidates)):
10                if candidates[i] > remaining:
11                    break
12                if i>start and candidates[i]==candidates[i-1]:
13                    continue
14                path.append(candidates[i])
15                helper(i+1, remaining-candidates[i], path)
16                path.pop()
17        
18        helper(0, target, [])
19        return res