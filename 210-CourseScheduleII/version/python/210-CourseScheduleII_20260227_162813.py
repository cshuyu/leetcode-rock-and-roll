# Last updated: 2/27/2026, 4:28:13 PM
1class Solution:
2    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
3        if endWord not in wordList:
4            return 0
5        graph = defaultdict(list)
6        for word in wordList:
7            for i in range(len(word)):
8                pattern = word[:i] + "*" + word[i+1:]
9                graph[pattern].append(word)
10        queue = deque([(beginWord, 1)])
11        visited = set()
12        while queue:
13            curr_word, curr_level = queue.popleft()
14            if curr_word == endWord:
15                return curr_level
16            for i in range(len(curr_word)):
17                pattern = curr_word[:i]+"*"+curr_word[i+1:]
18                for next_word in graph[pattern]:
19                    if next_word in visited:
20                        continue
21                    queue.append((next_word, curr_level+1))
22                    visited.add(next_word)
23        
24        return 0
25        
26
27        