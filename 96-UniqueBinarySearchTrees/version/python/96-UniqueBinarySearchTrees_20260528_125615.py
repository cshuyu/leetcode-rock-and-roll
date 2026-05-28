# Last updated: 5/28/2026, 12:56:15 PM
1"""
2O(Time) is O(n^2)
3O(Space) is O(n^2), stack: O(n), memo: O(n^2)
4"""
5class Solution:
6    def numTrees(self, n: int) -> int:
7        self.memo = {}
8        def findCount(low, high):
9            count = 0
10            if low>high:
11                return 1
12            if (low, high) in self.memo:
13                return self.memo[(low, high)]
14            # go through all root's possibilities
15            for i in range(low, high+1):
16                left_subtree_count = findCount(low, i-1)
17                right_subtree_count = findCount(i+1, high)
18                count += left_subtree_count * right_subtree_count
19            self.memo[(low, high)] = count
20            return count
21        
22        return findCount(1, n)
23