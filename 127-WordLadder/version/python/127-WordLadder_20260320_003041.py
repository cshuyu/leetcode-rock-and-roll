# Last updated: 3/20/2026, 12:30:41 AM
1class Solution:
2    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
3        if endWord not in wordList:
4            return 0
5        wordDict = defaultdict(list)
6        for word in wordList:
7            for i in range(len(word)):
8                pattern = word[:i] + "*" + word[i+1:]
9                wordDict[pattern].append(word)
10        
11        queue = deque()
12        queue.append((beginWord, 1))
13        visited = set()
14
15        while queue:
16            currWord, cnt = queue.popleft()
17            if currWord == endWord:
18                return cnt
19            for i in range(len(currWord)):
20                currPattern = currWord[:i] + "*" + currWord[i+1:]
21                if currPattern in wordDict:
22                    for nextWord in wordDict[currPattern]:
23                        if nextWord not in visited:
24                            queue.append((nextWord, cnt+1))
25                            visited.add(nextWord)
26        
27        return 0
28
29
30
31
32
33