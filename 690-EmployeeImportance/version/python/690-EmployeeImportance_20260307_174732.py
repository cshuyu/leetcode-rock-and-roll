# Last updated: 3/7/2026, 5:47:32 PM
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
12        employee_map = defaultdict(Employee)
13        for employee in employees:
14            employee_map[employee.id] = employee
15        # Complexity: time is O(n), space is O(n)
16        def dfs(id):
17            curr_employee = employee_map[id]
18            sum = curr_employee.importance
19            for next_employee_id in curr_employee.subordinates:
20                    sum += dfs(next_employee_id)
21            return sum
22
23        return dfs(id)