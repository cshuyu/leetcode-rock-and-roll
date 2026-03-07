# Last updated: 3/7/2026, 3:08:42 PM
1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        graph = defaultdict(list)
4        indegree = [0]*numCourses
5        res = []
6
7        for prerequisite in prerequisites:
8            from_course = prerequisite[1]
9            to_course = prerequisite[0]
10            graph[from_course].append(to_course)
11            indegree[to_course] += 1
12        
13        course_queue = deque()
14        for i in range(numCourses):
15            if indegree[i] == 0:
16                course_queue.append(i)
17        
18        while course_queue:
19            curr_course = course_queue.popleft()
20            res.append(curr_course)
21            for next_course in graph[curr_course]:
22                indegree[next_course] -= 1
23                if indegree[next_course] == 0:
24                    course_queue.append(next_course)
25        
26        if len(res)<numCourses:
27            return []
28        else:
29            return res
30
31