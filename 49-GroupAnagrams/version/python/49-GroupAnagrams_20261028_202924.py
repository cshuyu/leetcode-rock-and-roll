# Last updated: 10/28/2026, 8:29:24 PM
# Hashmap: the tuple is immutable and hashable
1'''
2Time: O(n*k)
3Space: O(n) --> if we view the key of 26 characters are O(1)
4'''
5class Solution:
6    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
7        groups = defaultdict(list)
8        for str in strs:
9            count = [0]*26
10            for char in str:
11                count[ord(char)-ord("a")] += 1
12            key = tuple(count)
13            groups[key].append(str)
14        return list(groups.values())
15
16