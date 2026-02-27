# Last updated: 2/27/2026, 1:13:06 AM
# Graph: Traverse shortest path(BFS)
1class Solution:
2    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
3        if endWord not in wordList:
4            return 0
5        
6        # 1. Build the Graph (Wildcard approach)
7        graph = defaultdict(list)
8        wordList.append(beginWord)
9        
10        for word in wordList:
11            for i in range(len(word)):
12                pattern = word[:i] + "*" + word[i+1:]
13                graph[pattern].append(word)
14                
15        # 2. Initialize BFS
16        # The queue stores a tuple: (current_word, current_path_length)
17        queue = deque([(beginWord, 1)])
18        visited = set([beginWord])
19        
20        # 3. Traverse the Graph
21        while queue:
22            current_word, level = queue.popleft()
23            
24            # If we reach the target, return the length immediately
25            if current_word == endWord:
26                return level
27            
28            # Find all neighbors using the wildcard patterns
29            for i in range(len(current_word)):
30                pattern = current_word[:i] + "*" + current_word[i+1:]
31                
32                for neighbor in graph[pattern]:
33                    if neighbor not in visited:
34                        visited.add(neighbor)
35                        queue.append((neighbor, level + 1))
36        
37        # If the queue empties and we never found the endWord
38        return 0
39