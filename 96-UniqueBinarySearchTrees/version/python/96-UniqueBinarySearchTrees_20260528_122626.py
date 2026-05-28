# Last updated: 5/28/2026, 12:26:26 PM
# BST: recursion+memo
1class Solution:
2    def numTrees(self, n: int) -> int:
3        self.memo = {}
4        def findCount(low, high):
5            count = 0
6            if low>high:
7                return 1
8            if (low, high) in self.memo:
9                return self.memo[(low, high)]
10            # go through all root's possibilities
11            for i in range(low, high+1):
12                left_subtree_count = findCount(low, i-1)
13                right_subtree_count = findCount(i+1, high)
14                count += left_subtree_count * right_subtree_count
15            self.memo[(low, high)] = count
16            return count
17        
18        return findCount(1, n)
19