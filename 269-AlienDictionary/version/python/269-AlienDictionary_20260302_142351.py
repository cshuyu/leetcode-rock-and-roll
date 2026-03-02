# Last updated: 3/2/2026, 2:23:51 PM
# Graph: Traverse with Topological sort(BFS)
1class Solution:
2    def alienOrder(self, words: List[str]) -> str:
3        graph = {c: set() for word in words for c in word}
4        indegree = {c: 0 for c in graph}
5        res = []
6
7        def buildGraph(word1, word2, graph, indegree):
8            for from_char, to_char in zip(word1, word2):
9                if from_char!=to_char:
10                    if to_char not in graph[from_char]:
11                        graph[from_char].add(to_char)
12                        indegree[to_char] += 1
13                    return
14
15        for i in range(len(words)-1):
16            word1 = words[i]
17            word2 = words[i+1]
18            if len(word1)>len(word2) and word1.startswith(word2):
19                return ""
20            buildGraph(word1, word2, graph, indegree)
21        
22        queue = deque()
23        for node in graph.keys():
24            if indegree[node] == 0:
25                queue.append(node)
26
27        while queue:
28            curr_node = queue.popleft()
29            res.append(curr_node)
30            for next_node in graph[curr_node]:
31                indegree[next_node] -= 1
32                if indegree[next_node] == 0:
33                    queue.append(next_node)
34
35        if len(res) != len(graph):
36            return ""
37        else:
38            return "".join(res)