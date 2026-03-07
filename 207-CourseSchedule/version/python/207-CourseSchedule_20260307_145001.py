# Last updated: 3/7/2026, 2:50:01 PM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        # Space Complexity: O(v)+O(E)
4        graph = defaultdict(list)
5        indegree = [0]*numCourses
6        res = []
7        # Time Complexity: O(E)
8        for prerequisite in prerequisites:
9            from_course = prerequisite[1]
10            to_course =  prerequisite[0]
11            graph[from_course].append(to_course)
12            indegree[to_course] += 1
13        
14        course_queue = deque()
15        # Time Complexity: O(V)
16        for i in range(numCourses):
17            if indegree[i]==0:
18                course_queue.append(i)
19        
20        while course_queue:
21            curr = course_queue.popleft()
22            res.append(curr)
23            for next in graph[curr]:
24                indegree[next] -= 1
25                if indegree[next] == 0:
26                    course_queue.append(next)
27
28        for i in range(numCourses):
29            if indegree[i] != 0:
30                return False
31        return True