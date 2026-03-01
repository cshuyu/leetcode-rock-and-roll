# Last updated: 2/28/2026, 11:44:32 PM
# Graph: Traverse(BFS) to find shortest path
1class Solution:
2    def minJumps(self, arr: List[int]) -> int:
3        valueMap = defaultdict(list)
4        for i in range(len(arr)):
5            valueMap[arr[i]].append(i)
6
7        queue = deque()
8        queue.append((arr[0], 0, 0))
9        visited = set()
10        visited.add(0)
11
12        while queue:
13            curr_val, curr_index, cnt = queue.popleft()
14            if curr_index == len(arr)-1:
15                return cnt
16            if curr_index+1<len(arr) and curr_index+1 not in visited:
17                visited.add(curr_index+1)
18                queue.append((arr[curr_index+1], curr_index+1, cnt+1))
19            if curr_index-1>=0 and curr_index-1 not in visited:
20                visited.add(curr_index-1)
21                queue.append((arr[curr_index-1], curr_index-1, cnt+1))
22            for next_index in valueMap[curr_val]:
23                if next_index not in visited:
24                    queue.append((curr_val, next_index, cnt+1))
25                    visited.add(next_index)
26            valueMap[curr_val].clear()
27        
28        return 0
29
30
31
32