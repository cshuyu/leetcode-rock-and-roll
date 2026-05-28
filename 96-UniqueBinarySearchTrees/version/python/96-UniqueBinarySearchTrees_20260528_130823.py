# Last updated: 5/28/2026, 1:08:23 PM
# BST: recursion+range_based_memo
1"""
2Further optimiation with range-based memo
3Time complexity: O(n)
4Space complexity: O(n), both stack and memo is O(n)
5"""
6class Solution:
7    def numTrees(self, n: int) -> int:
8        self.memo = {}
9        # based on range
10        def findCount(total_node):
11            count = 0
12            if total_node==0:
13                return 1
14            if total_node in self.memo:
15                return self.memo[total_node]
16            for i in range(total_node):
17                left_count = findCount(i)
18                right_count = findCount(total_node-i-1)
19                count += left_count * right_count
20            self.memo[total_node] = count
21            return count
22        
23        return findCount(n)
24
25        