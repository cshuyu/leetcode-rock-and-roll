# Last updated: 2/25/2026, 5:13:23 PM
# Graph: traverse(DFS)
1"""
2# Definition for Employee.
3class Employee:
4    def __init__(self, id: int, importance: int, subordinates: List[int]):
5        self.id = id
6        self.importance = importance
7        self.subordinates = subordinates
8"""
9
10class Solution:
11    def getImportance(self, employees: List['Employee'], id: int) -> int:
12        map = {e.id: e for e in employees}
13        def helper(employee):
14            sum = employee.importance
15            for next_id in employee.subordinates:
16                sum += helper(map[next_id])
17            return sum
18        return helper(map[id])
19