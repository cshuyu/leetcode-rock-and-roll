# Last updated: 2/23/2026, 6:44:42 PM
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt_set = {}
        for i in arr:
            cnt_set[i] = cnt_set.get(i, 0)+1
        
        return len(cnt_set) == len(set(cnt_set.values()))
             